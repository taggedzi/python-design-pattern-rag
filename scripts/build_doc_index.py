# Path: scripts/build_doc_index.py
# pylint: disable=logging-fstring-interpolation
"""Builds a documentation index file from all .md files in a directory."""
import argparse
import logging
from pathlib import Path

# --- Directory setup ---
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent

def setup_logging():
    """Sets up logging with a basic configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s'
    )
    return logging.getLogger(__name__)

logger = setup_logging()

def build_index(docs_dir: Path, index_file: Path) -> None:
    """
    Scan the docs_dir for Markdown files and write an index_file
    listing each with a relative Markdown link.
    """
    md_files = sorted(
        f for f in docs_dir.iterdir()
        if f.is_file() and f.suffix.lower() == '.md' and f.name != index_file.name
    )
    lines = ['# Documentation Index', '']
    for f in md_files:
        rel = f.relative_to(docs_dir)
        title = f.stem.replace('_', ' ').replace('-', ' ').title()
        lines.append(f'- [{title}]({rel.as_posix()})')
    content = '\n'.join(lines) + '\n'
    index_file.write_text(content, encoding='utf-8')
    logger.info(f'Wrote documentation index: {index_file}')

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Build an index.md in the docs folder listing all Markdown files.'
    )
    parser.add_argument(
        '--docs',
        default=str(project_root / 'docs'),
        help='Directory containing documentation Markdown files'
    )
    parser.add_argument(
        '--output',
        default='index.md',
        help='Name of the generated index file within the docs directory'
    )
    args = parser.parse_args()

    docs_dir = Path(args.docs)
    if not docs_dir.is_dir():
        logger.error(f'Provided docs path is not a directory: {docs_dir}')
        return

    index_file = docs_dir / args.output
    build_index(docs_dir, index_file)

if __name__ == '__main__':
    main()
