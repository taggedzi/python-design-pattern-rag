# The Sentinel Object Pattern (Behavioral)

## Intent

The Sentinel Object pattern signals special conditions or end-of-sequence markers in a program. It helps distinguish between user-provided values and missing values, which is useful for handling optional arguments or data stream termination.

## Problem It Solves

This Sentinel Object pattern solves the problem of distinguishing between user input (including `None`) and the absence of a value. It's especially useful with optional parameters, allowing you to tell whether a value was explicitly provided or left out.

## When to Use It

Use Sentinel Object pattern when you need to handle special cases in your code and clearly separate user-provided values, `None`, and control signals like end-of-sequence markers.

## When NOT to Use It

Avoid using the Sentinel Object pattern for required arguments. In those cases, inputs should be validated at the start of the function or method.

## How It Works

Create a unique, identifiable object—a "sentinel"—for each special condition. These are usually instances of a `Sentinel` class with a clear name. The `process_items` function in the example shows how sentinels can signal different conditions.

## Real-World Analogy

Imagine a party with two special guests: one always brings food and the other drinks. If a guest brings neither, it signals the party is over. These roles represent different sentinel values.

## Simplified Example

```python
class Sentinel:
    def __init__(self, name):
        self.name = name

# Define sentinels for special conditions
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

## See Also

The Sentinel Object Pattern appears in many programming languages, including Python. A sample implementation can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/sentinel.py).
