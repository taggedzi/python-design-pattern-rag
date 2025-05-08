# Path: scripts/generate_lessons.py
# pylint: disable=broad-exception-caught,logging-fstring-interpolation,line-too-long
"""Generate lessons from the patterns folder."""
import argparse
import logging
import json
import re
from pathlib import Path
from typing import Optional, Tuple, List
import httpx

# --- Directory setup ---
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

SYSTEM_PROMPT = """
You are a senior Python instructor. When given a Python file that demonstrates a design pattern you generate a well-structured and very comprehensive lesson for a user with a 10th grade level education who is familiar with the basics of python..
You use properly formatted Markdown with its allowed attributes to make your lesson easy to read and engaging. 
You verify each section for completeness and acuracy before moving to the next. 

Structure your output like this:

# The <Pattern Name> Pattern (<Category>)

## Intent

Brief description of the pattern’s purpose.

## Problem It Solves

What kind of design or architectural problem it addresses.

## When to Use It

Key use cases for applying the pattern.

## When NOT to Use It

When the pattern is not ideal or overkill.

## How It Works

Key classes/functions and their interaction.

## Real-World Analogy

Relatable metaphor for the pattern.

## Simplified Example

Include a short example or pseudocode. Use Markdown code block syntax.

## See Also

Provide a Markdown link to the corresponding Python file in the repo.
"""

# Required headers in each lesson
REQUIRED_SECTIONS = [
    r"^# The .+ Pattern",
    r"^## Intent",
    r"^## Problem It Solves",
    r"^## When to Use It",
    r"^## When NOT to Use It",
    r"^## How It Works",
    r"^## Real-World Analogy",
    r"^## Simplified Example",
    r"^## See Also"
]


def is_valid_lesson(text: str) -> bool:
    """Check that all required sections are present in the lesson text."""
    return all(re.search(pat, text, re.MULTILINE) for pat in REQUIRED_SECTIONS)


def call_ollama_model(model: str, system_prompt: str, user_prompt: str) -> Optional[str]:
    """Call the Ollama model and return the output."""
    try:
        response = httpx.post(
            "http://localhost:11434/api/chat",
            json={
                "model": model,
                "stream": True,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user",   "content": user_prompt},
                ],
            },
            timeout=120.0
        )
        response.raise_for_status()

        full_output = []
        for line in response.iter_lines():
            if not line or line.strip() == '':
                continue
            try:
                data = json.loads(line)
                content = data.get("message", {}).get("content")
                if content:
                    full_output.append(content)
            except Exception as e:
                logging.warning(f"Failed to parse chunk: {line[:80]}... - {e}")
        return "".join(full_output).strip()

    except Exception as e:
        logging.error(f"Ollama request failed: {e}")
        return None


def extract_title_and_category(path: Path) -> Tuple[str, str]:
    """Extract the title and category of a file in the patterns directory."""
    parts = path.relative_to(script_dir.parent / 'patterns').parts
    category = parts[0].capitalize() if parts else 'General'
    name = path.stem.replace('_', ' ').title()
    return name, category


def generate_lessons(
    source_dir: Path,
    output_dir: Path,
    model: str = "lesson-planner:latest"
) -> None:
    """Generate lessons from Python files."""
    # Prepare output
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    failures: List[Path] = []

    # Walk source patterns
    py_files = sorted(source_dir.rglob("*.py"))
    logging.info(f"Found {len(py_files)} Python pattern files in {source_dir}.")

    for file_path in py_files:
        name, category = extract_title_and_category(file_path)
        filename = f"{category.lower()}_{file_path.stem}.md"
        out_path = output_dir / filename

        # Skip if lesson already exists
        if out_path.exists():
            logging.info(f"Skipping existing lesson: {out_path.name}")
            continue

        logging.info(f"Generating lesson for {name} ({category})")
        code = file_path.read_text(encoding="utf-8")
        user_prompt = f"""
Below is the full implementation of the Python '{name}' pattern from the '{category}' category:

```python
{code}
```

Please generate a Markdown-based educational lesson as described in the system prompt.
"""
        lesson = call_ollama_model(model, SYSTEM_PROMPT, user_prompt)

        # Validate before saving
        if lesson and is_valid_lesson(lesson):
            out_path.write_text(lesson, encoding="utf-8")
            logging.info(f"✅ Wrote lesson: {out_path.name}")
        else:
            logging.warning(f"❌ Invalid or empty lesson for {file_path.stem}")
            failures.append(file_path)

    # Log failures
    if failures:
        fail_log = output_dir / 'failed_lessons.log'
        with fail_log.open('w', encoding='utf-8') as lf:
            for p in failures:
                lf.write(p.as_posix() + '\n')
        logging.warning(f"{len(failures)} lessons failed; see {fail_log}")
    else:
        logging.info("All lessons generated successfully.")


def main() -> None:
    """The Main function."""
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s'
    )
    parser = argparse.ArgumentParser(
        description="Generate Python lesson Markdown files using Ollama, with incremental and validation features."
    )
    parser.add_argument(
        '--source',
        default=str(project_root / 'patterns'),
        help='Directory containing Python source patterns'
    )
    parser.add_argument(
        '--output',
        default=str(project_root / 'docs'),
        help='Directory to write Markdown lessons'
    )
    parser.add_argument(
        '--model',
        default='lesson-planner:latest',
        help='Ollama model to use (default: lesson-planner:latest)'
    )
    args = parser.parse_args()

    generate_lessons(
        source_dir=Path(args.source),
        output_dir=Path(args.output),
        model=args.model
    )

if __name__ == '__main__':
    main()
