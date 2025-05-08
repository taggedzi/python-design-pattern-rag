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
    front_matter: Dict[str, str] = {}
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
    index: List[Dict[str, str]] = []
    for file in sorted(chunk_dir.glob("*.md")):
        text = file.read_text(encoding='utf-8')
        front = parse_front_matter(text)
        summary = extract_summary(text)

        # Determine file path and chunk
        file_rel = front.get("file", file.name)
        chunk_name = front.get("chunk", file.stem)

        # Derive pattern name: use front matter if present, else infer from file name
        pattern = front.get("pattern", "")
        if not pattern:
            # e.g., 'structural/global_object.py' -> 'global_object' -> 'Global Object'
            stem = Path(file_rel).stem
            pattern = stem.replace('_', ' ').title()

        entry = {
            "file": file_rel,
            "chunk": chunk_name,
            "pattern": pattern,
            "summary": summary
        }
        index.append(entry)
    return index


def save_json(index: List[Dict[str, str]], output_path: Path):
    """Saves the summary index as a JSON file."""
    output_path.write_text(json.dumps(index, indent=2), encoding='utf-8')


def main():
    """Main function for building the summary index."""
    parser = argparse.ArgumentParser(
        description="Build a summary index from markdown chunks."
    )
    parser.add_argument(
        "input", help="Directory containing markdown chunks"
    )
    parser.add_argument(
        "output", help="Path to save the JSON index"
    )
    args = parser.parse_args()

    chunk_dir = Path(args.input).resolve()
    output_path = Path(args.output).resolve()

    index = build_summary_index(chunk_dir)
    save_json(index, output_path)
    logger.info(f"Summary index saved to: {output_path} ({len(index)} entries)")


if __name__ == "__main__":
    main()
