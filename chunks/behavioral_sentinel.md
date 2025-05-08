---
file: behavioral/sentinel.py
chunk: behavioral_sentinel.md
---

```python
"""
Sentinel Object Pattern Example

The Sentinel Object Pattern uses unique, distinguishable objects (sentinels) to signal
special conditions—like missing arguments or end-of-sequence markers—in a program. This
allows you to differentiate between user-provided values (including None) and the absence
of a value or a special control signal.

Pattern Type: Utility / Behavioral Micro‑pattern
"""

class Sentinel:
    """
    A simple sentinel class. Each instance is unique and identifiable by name.
    """
    __slots__ = ("name",)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"<Sentinel {self.name}>"

# Define sentinel instances for common use-cases
MISSING = Sentinel("MISSING")
END_OF_STREAM = Sentinel("END_OF_STREAM")


def process_items(iterator, max_items=MISSING):
    """
    Processes items from an iterator up to max_items.
    - If max_items is MISSING, processes all items.
    - If max_items is None, treats it as zero and does nothing.

    This demonstrates using a sentinel to differentiate "no argument provided" from
    "argument explicitly set to None".
    """
    if max_items is MISSING:
        print("Processing all items.")
    elif max_items is None:
        print("No items to process (max_items=None).")
        return
    else:
        print(f"Processing up to {max_items} items.")

    count = 0
    for item in iterator:
        if max_items is not MISSING and max_items is not None and count >= max_items:
            break
        print(f"Item {count}: {item}")
        count += 1


def stream_data(data):
    """
    Simulate streaming data: yields each item, then an END_OF_STREAM sentinel.
    """
    for item in data:
        yield item
    yield END_OF_STREAM


def consume_stream(stream):
    """
    Consumes a stream until the END_OF_STREAM sentinel is encountered.
    """
    print("Starting stream consumption...")
    for value in stream:
        if value is END_OF_STREAM:
            print("Received END_OF_STREAM sentinel. Stopping.")
            break
        print(f"Consumed: {value}")


def main():
    """The main function to demonstrate the the sentinel pattern."""
    items = list(range(3))

    print("--- Example 1: process_items (all) ---")
    process_items(items)

    print("\n--- Example 2: process_items (limit=2) ---")
    process_items(items, max_items=2)

    print("\n--- Example 3: process_items (max_items=None) ---")
    process_items(items, max_items=None)

    print("\n--- Example 4: stream consumption with sentinel ---")
    data_stream = stream_data(["a", "b", "c"])
    consume_stream(data_stream)


if __name__ == "__main__":
    main()

```

## Summary
Demonstration of the Sentinel Object Pattern in Python.

## Docstrings
- A simple sentinel class. Each instance is unique and identifiable by name.
- Processes items from an iterator up to max_items. - If max_items is MISSING, processes all items. - If max_items is None, treats it as zero and does nothing. This demonstrates using a sentinel to differentiate "no argument provided" from "argument explicitly set to None".
- Simulate streaming data: yields each item, then an END_OF_STREAM sentinel.
- Consumes a stream until the END_OF_STREAM sentinel is encountered.

