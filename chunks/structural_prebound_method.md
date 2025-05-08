---
file: structural/prebound_method.py
chunk: structural_prebound_method.md
---

```python
"""
Prebound Method Pattern Example

Demonstrates how to use the Prebound Method pattern in Python to improve clarity,
performance, and decouple method lookup. Commonly used when repeatedly calling object
methods in loops or registering callbacks.
"""

from functools import partial
from time import perf_counter


class Processor:
    """
    Processor provides different processing methods for various data types.
    """
    def process_text(self, text: str) -> None:
        """Handle processing of text data."""
        print(f"[process_text] Processing text: {text}")

    def process_numbers(self, numbers: list) -> None:
        """Handle processing of numeric lists."""
        print(f"[process_numbers] Processing numbers: {numbers}")


def demonstrate_prebound_methods():
    """
    Compare calling methods with and without prebinding within a loop.
    """
    proc = Processor()
    tasks = [
        ("text", "Hello"),
        ("numbers", [1, 2, 3]),
        ("text", "World"),
        ("numbers", [4, 5, 6])
    ]

    # --- Without prebinding: dynamic lookup each iteration ---
    start = perf_counter()
    for kind, value in tasks:
        # getattr lookup on each loop iteration
        handler = getattr(proc, f"process_{kind}")
        handler(value)
    no_bind_time = perf_counter() - start
    print(f"\nTime without prebinding: {no_bind_time:.6f} seconds\n")

    # --- With prebinding: bind instance methods to locals ---
    start = perf_counter()
    process_text = proc.process_text
    process_numbers = proc.process_numbers
    for kind, value in tasks:
        if kind == "text":
            process_text(value)
        else:
            process_numbers(value)
    bound_time = perf_counter() - start
    print(f"Time with prebinding: {bound_time:.6f} seconds\n")

    # --- Manual binding via descriptor protocol ---
    bound_via_descriptor = Processor.process_text.__get__(proc, Processor)
    bound_via_descriptor("Bound via descriptor")

    # --- Using functools.partial to prebind arguments ---
    print()
    say_hello = partial(proc.process_text, "Hello via partial")
    say_numbers = partial(proc.process_numbers, [7, 8, 9])
    say_hello()
    say_numbers()


if __name__ == "__main__":
    demonstrate_prebound_methods()

```

## Summary
Demonstrates the Prebound Method pattern in Python to improve clarity, performance, and decouple method lookup. Compares calling methods with and without prebinding within a loop.

## Docstrings
- Processor provides different processing methods for various data types.
- Handle processing of text data.
- Handle processing of numeric lists.
- Compare calling methods with and without prebinding within a loop.

