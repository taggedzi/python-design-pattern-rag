#!/usr/bin/env python3
import argparse
import logging
import json
import httpx
from pathlib import Path
from typing import Optional, Tuple

# --- Directory setup ---
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')

SYSTEM_PROMPT = """
You are a senior Python instructor. When given a Python file that demonstrates a design pattern, generate a well-structured, beginner-friendly Markdown lesson.

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

def call_ollama_model(model: str, system_prompt: str, user_prompt: str) -> Optional[str]:
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
            line = line.strip()
            if not line:
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
    parts = path.parts
    category = parts[-2].capitalize() if len(parts) > 1 else "General"
    name = path.stem.replace('_', ' ').title()
    return name, category


def generate_lessons(source_dir: str, output_dir: str, model: str = "lesson-planner") -> None:
    source_path = Path(source_dir)
    output_path = Path(output_dir)
    if output_path.exists():
        for f in output_path.iterdir():
            if f.is_file():
                f.unlink()
    else:
        output_path.mkdir(parents=True, exist_ok=True)

    py_files = list(source_path.rglob("*.py"))
    logging.info(f"Found {len(py_files)} Python pattern files in {source_path}.")

    for file_path in py_files:
        name, category = extract_title_and_category(file_path)
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

        if lesson:
            filename = f"{category.lower()}_{file_path.stem}.md"
            out_path = output_path / filename
            out_path.write_text(lesson, encoding="utf-8")
            logging.info(f"✅ Wrote lesson: {out_path}")
        else:
            logging.warning(f"❌ Failed lesson for {file_path}")


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s'
    )
    parser = argparse.ArgumentParser(
        description="Generate Python lesson Markdown files using Ollama."
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
        source_dir=args.source,
        output_dir=args.output,
        model=args.model
    )

if __name__ == '__main__':
    main()
