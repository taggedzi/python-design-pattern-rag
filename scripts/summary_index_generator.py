"""Script to generate a summary index file based on the contents of Markdown files."""
# pylint: disable=logging-fstring-interpolation
import argparse
import json
import logging
import re
from pathlib import Path
from typing import List, Dict

def setup_logging():
    """Sets up logging with a basic configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s'
    )
    return logging.getLogger(__name__)

logger = setup_logging()

def parse_front_matter(text: str) -> Dict[str, str]:
    """Extracts YAML-like front matter from markdown text."""
    front_matter = {}
    if text.startswith("---"):
        lines = text.splitlines()
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if ':' in line:
                key, value = line.split(':', 1)
                front_matter[key.strip()] = value.strip()
    return front_matter

def extract_summary(text: str) -> str:
    """Extracts the content under the ## Summary section."""
    match = re.search(r"## Summary\n(.+?)\n## ", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    match = re.search(r"## Summary\n(.+)$", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def build_summary_index(chunk_dir: Path) -> List[Dict[str, str]]:
    """Builds a summary index from markdown chunk files."""
    index = []
    for file in sorted(chunk_dir.glob("*.md")):
        with open(file, encoding="utf-8") as f:
            text = f.read()

        front = parse_front_matter(text)
        summary = extract_summary(text)

        entry = {
            "file": front.get("file", file.name),
            "chunk": front.get("chunk", file.stem),
            "pattern": front.get("pattern", ""),
            "summary": summary
        }
        index.append(entry)
    return index

def save_json(index: List[Dict[str, str]], output_path: Path):
    """Saves the summary index as a JSON file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)

def main():
    """Main function for building the summary index."""
    parser = argparse.ArgumentParser(description="Build a summary index from markdown chunks.")
    parser.add_argument("input", help="Directory containing markdown chunks")
    parser.add_argument("output", help="Path to save the JSON index")
    args = parser.parse_args()

    chunk_dir = Path(args.input)
    output_path = Path(args.output)

    index = build_summary_index(chunk_dir)
    save_json(index, output_path)
    logger.info(f"Summary index saved to: {output_path.resolve()} ({len(index)} entries)")


if __name__ == "__main__":
    main()
