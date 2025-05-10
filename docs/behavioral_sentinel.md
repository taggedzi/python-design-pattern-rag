# The Sentinel Object Pattern (Behavioral)

## Purpose

The Sentinel Object pattern is used to represent special values or conditions in a program—like missing data or the end of a sequence. It helps you clearly distinguish between user-provided values, `None`, and control signals.

## The Problem It Solves

Sometimes, it's hard to tell whether a function parameter was explicitly passed as `None` or not provided at all. This pattern solves that by introducing a unique sentinel object that signals a special condition, helping you avoid confusion and write cleaner, more predictable code.

## When to Use It

Use this pattern when:

* You need to detect whether an argument was passed at all.
* You want to avoid using `None` for multiple meanings (e.g., both "no value" and "explicitly set to none").
* You’re working with iterators or streams and need to indicate the end of input.

## When NOT to Use It

Avoid this pattern when:

* You're dealing with required arguments—just validate those directly.
* Simpler constructs like `None` or empty lists are sufficient for your use case.
* You need thread safety, and the sentinels might be shared across threads (you’ll need to take extra care in those cases).

## How It Works

A sentinel is a unique object—often an instance of a class like `Sentinel`—used to represent a specific condition. It doesn’t equal any other value and is used with identity checks (e.g., `is FOOD`). You can define as many sentinels as you need for different scenarios.

## Real-World Analogy

Imagine a party where certain guests bring either food or drinks. If someone arrives with neither, it means the party is over. Each role (food, drinks, no more guests) can be represented by a distinct sentinel object.

## Simplified Example

```python
class Sentinel:
    def __init__(self, name):
        self.name = name

# Create unique sentinel objects
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

In this example, `FOOD`, `DRINK`, and `END_OF_PARTY` are sentinel values used to represent different conditions. The function uses identity checks (`is`) to decide what to do.

## Learn More

For a full example, check the Python implementation here:
[Sentinel Object Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/sentinel.py)
