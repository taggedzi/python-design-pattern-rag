# The Prebound Method Pattern (Structural)

## Purpose

The Prebound Method pattern improves performance by storing a method reference in a local variable before calling it repeatedly. It’s especially helpful in loops or callback-heavy code, where method lookups would otherwise happen over and over.

## Problem It Solves

In Python, each time you call an instance method (e.g., `obj.method()`), Python performs a dynamic lookup to resolve the method. This is fine for occasional calls, but in tight loops or high-frequency callbacks, this lookup adds unnecessary overhead. By assigning the method to a local variable first, you can avoid the repeated lookup and make calls faster.

## When to Use It

Use this pattern when:

* You call the same method many times in a loop or performance-critical section.
* You’re registering the same method as a callback in multiple places.
* You want to optimize by reducing small but repeated overhead.

## When Not to Use It

Skip this pattern if:

* The method is only called a few times.
* Readability matters more than micro-optimization.
* The performance gain is too small to justify the extra step.

## How It Works

Instead of calling the method like this each time:

```python
obj.method()
```

You assign it once to a local variable:

```python
method = obj.method
```

Then use `method()` directly. In Python, this works because accessing a bound method returns a callable object that includes the instance (`self`), so you're effectively storing a preconfigured function.

## Real-World Analogy

Think of a librarian who looks up a specific book multiple times. Rather than scanning all the shelves each time, they write the book’s location on a sticky note and go directly to it. That’s what prebinding does—it skips the repeated search.

## Simplified Example

```python
class Processor:
    def process_text(self, text):
        print(f"Processing text: {text}")

proc = Processor()

# Prebind the method
process_text = proc.process_text

# Use it multiple times
for _ in range(3):
    process_text("Hello, world!")
```

By prebinding `proc.process_text` to `process_text`, you avoid the repeated attribute lookup during the loop.

## Learn More

Explore the full Python example here:
[Prebound Method Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/prebound_method.py)
