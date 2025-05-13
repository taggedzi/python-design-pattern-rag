# The Sentinel Object Pattern (Behavioral)

## Purpose

The Sentinel Object pattern uses unique objects to represent special conditions or values—like missing data or the end of a sequence. It helps you clearly distinguish between user input, default values like `None`, and control signals.

## Problem It Solves

In Python, it's sometimes unclear whether `None` was explicitly passed to a function or used as a default. This can lead to bugs when `None` has multiple meanings. The Sentinel Object pattern solves this by introducing a unique object that stands for a specific condition, making your code clearer and easier to maintain.

## When to Use It

Use this pattern when:

* You need to know if a function argument was passed explicitly.
* You want to avoid overloading `None` with multiple meanings.
* You're processing data streams or iterators and need a special marker (e.g., end of input).

## When Not to Use It

Avoid this pattern if:

* You're working with required parameters—just validate them directly.
* `None`, `False`, or an empty list is clear and sufficient.
* You're in a multi-threaded environment where shared sentinel values may cause issues (unless handled carefully).

## How It Works

A sentinel is a unique, standalone object—usually an instance of a small custom class. It doesn't compare equal to any regular value and is checked using `is` rather than `==`. You can define multiple sentinels to represent different special states.

## Real-World Analogy

Imagine a party where guests are expected to bring food or drinks. If someone shows up with neither, it signals the party is over. Each role—food, drinks, or no more guests—can be represented by a unique sentinel.

## Simplified Example

```python
class Sentinel:
    def __init__(self, name):
        self.name = name

# Create sentinel objects
FOOD = Sentinel("Food")
DRINK = Sentinel("Drink")
END_OF_PARTY = Sentinel("End of Party")

def party_guest(item):
    if item is FOOD:
        print("This guest brought food.")
    elif item is DRINK:
        print("This guest brought drinks.")
    else:
        print("No more guests at the party.")

# Usage
party_guest(FOOD)
party_guest(DRINK)
party_guest(END_OF_PARTY)
```

In this example, each sentinel represents a different condition. The function checks which sentinel was passed using `is` to determine the behavior.

## Learn More

See the full implementation here:
[Sentinel Object Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/sentinel.py)
