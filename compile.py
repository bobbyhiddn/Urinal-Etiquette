#!/usr/bin/env python3
"""
Book Compiler for Urinal Strategy

Assembles all prose.md files into a single compiled book with table of contents.
Output goes to compiled/book.md

Usage:
    python compile.py
    python compile.py --output compiled/book.md
"""

import os
import re
import argparse
from pathlib import Path
from datetime import datetime

# Book structure - order matters
BOOK_STRUCTURE = [
    {
        "type": "frontmatter",
        "title": "Urinal Strategy",
        "subtitle": "The Ethics of Making the Correct Decision"
    },
    {
        "type": "section",
        "path": "sections/prelude/prose.md",
        "toc_title": "Prelude: The Geometry Exists"
    },
    {
        "type": "part",
        "title": "Part I: Seeing the Room",
        "epigraph": "Before you can position, you must perceive."
    },
    {
        "type": "section",
        "path": "sections/part-1/chapter-1/prose.md",
        "toc_title": "Chapter 1: Urinal Strategy"
    },
    {
        "type": "section",
        "path": "sections/part-1/chapter-2/prose.md",
        "toc_title": "Chapter 2: Most People Aren't Playing"
    },
    {
        "type": "section",
        "path": "sections/part-1/chapter-3/prose.md",
        "toc_title": "Chapter 3: The Diagnostic Method"
    },
    {
        "type": "part",
        "title": "Part II: The Tools",
        "epigraph": "Principles for positioning and communication."
    },
    {
        "type": "section",
        "path": "sections/part-2/chapter-4/prose.md",
        "toc_title": "Chapter 4: The Vacuum Principle"
    },
    {
        "type": "section",
        "path": "sections/part-2/chapter-5/prose.md",
        "toc_title": "Chapter 5: Hesitation as Risk"
    },
    {
        "type": "section",
        "path": "sections/part-2/chapter-6/prose.md",
        "toc_title": "Chapter 6: Moving First"
    },
    {
        "type": "section",
        "path": "sections/part-2/chapter-7/prose.md",
        "toc_title": "Chapter 7: The Soft Tongue"
    },
    {
        "type": "section",
        "path": "sections/part-2/chapter-8/prose.md",
        "toc_title": "Chapter 8: Proverbs 25"
    },
    {
        "type": "part",
        "title": "Part III: The Games",
        "epigraph": "Understanding what you're playing."
    },
    {
        "type": "section",
        "path": "sections/part-3/chapter-9/prose.md",
        "toc_title": "Chapter 9: Finite vs Infinite"
    },
    {
        "type": "section",
        "path": "sections/part-3/chapter-10/prose.md",
        "toc_title": "Chapter 10: The Chopping Block Ethic"
    },
    {
        "type": "section",
        "path": "sections/part-3/chapter-11/prose.md",
        "toc_title": "Chapter 11: Information Over Safety"
    },
    {
        "type": "part",
        "title": "Part IV: The Ethics",
        "epigraph": "Constraints on the game."
    },
    {
        "type": "section",
        "path": "sections/part-4/chapter-12/prose.md",
        "toc_title": "Chapter 12: Wise as Serpents, Innocent as Doves"
    },
    {
        "type": "section",
        "path": "sections/part-4/chapter-13/prose.md",
        "toc_title": "Chapter 13: The Trap of Being Correct"
    },
    {
        "type": "section",
        "path": "sections/part-4/chapter-14/prose.md",
        "toc_title": "Chapter 14: Finding Your Stall"
    },
    {
        "type": "part",
        "title": "Part V: The Weight",
        "epigraph": "What to do when it descends."
    },
    {
        "type": "section",
        "path": "sections/part-5/chapter-15/prose.md",
        "toc_title": "Chapter 15: The Shiver Is Universal"
    },
    {
        "type": "section",
        "path": "sections/part-5/chapter-16/prose.md",
        "toc_title": "Chapter 16: The Staircase Appears"
    },
    {
        "type": "section",
        "path": "sections/part-5/chapter-17/prose.md",
        "toc_title": "Chapter 17: Positioning and Providence"
    },
]


def get_root_dir():
    """Get the root directory of the book project."""
    return Path(__file__).parent


def read_prose_file(filepath):
    """Read a prose.md file and return its contents."""
    full_path = get_root_dir() / filepath
    if full_path.exists():
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    return None


def generate_toc(structure):
    """Generate table of contents from book structure."""
    toc_lines = ["## Table of Contents\n"]

    for item in structure:
        if item["type"] == "section":
            content = read_prose_file(item["path"])
            if content:
                toc_lines.append(f"- {item['toc_title']}")
            else:
                toc_lines.append(f"- {item['toc_title']} *(not yet written)*")
        elif item["type"] == "part":
            toc_lines.append(f"\n**{item['title']}**\n")

    return "\n".join(toc_lines)


def compile_book(output_path):
    """Compile all prose.md files into a single book."""
    root = get_root_dir()
    output = []
    sections_found = 0
    sections_missing = 0

    for item in BOOK_STRUCTURE:
        if item["type"] == "frontmatter":
            output.append(f"# {item['title']}")
            output.append(f"## {item['subtitle']}\n")
            output.append("---\n")
            output.append(generate_toc(BOOK_STRUCTURE))
            output.append("\n---\n")

        elif item["type"] == "part":
            output.append(f"\n---\n\n# {item['title']}\n")
            if item.get("epigraph"):
                output.append(f"*{item['epigraph']}*\n")
            output.append("---\n")

        elif item["type"] == "section":
            content = read_prose_file(item["path"])
            if content:
                output.append(f"\n{content}\n")
                sections_found += 1
            else:
                output.append(f"\n## {item['toc_title']}\n")
                output.append("*This chapter has not yet been written.*\n")
                sections_missing += 1

    # Add compilation metadata
    output.append("\n---\n")
    output.append(f"\n*Compiled on {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
    output.append(f"*Sections complete: {sections_found}/{sections_found + sections_missing}*\n")

    # Write output
    output_file = root / output_path
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(output))

    print(f"Book compiled to: {output_file}")
    print(f"Sections found: {sections_found}")
    print(f"Sections missing: {sections_missing}")

    return sections_found, sections_missing


def main():
    parser = argparse.ArgumentParser(description="Compile Urinal Strategy book")
    parser.add_argument(
        "--output", "-o",
        default="compiled/book.md",
        help="Output file path (default: compiled/book.md)"
    )
    args = parser.parse_args()

    compile_book(args.output)


if __name__ == "__main__":
    main()
