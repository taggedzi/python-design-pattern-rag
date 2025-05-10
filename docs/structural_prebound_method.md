# The Prebound Method Pattern (Structural)

## Purpose

The Prebound Method pattern improves performance and reduces overhead by storing a method reference in a local variable. This is especially useful when you need to call the same method repeatedly, such as inside loops or when registering callbacks.

## The Problem It Solves

In Python, calling an instance method involves a dynamic lookup—it checks the object’s dictionary and method resolution order every time. While this is fine for occasional calls, it can be a performance bottleneck in tight loops or high-frequency callback systems. Prebinding the method to a local variable removes the repeated lookup, making method calls faster.

## When to Use It

Use this pattern when:

* You're calling an instance method many times in a loop or frequently within performance-sensitive code.
* You're registering or reusing the same method as a callback in multiple places.
* You want to minimize the slight but cumulative cost of repeated method lookup.

## When NOT to Use It

Avoid this pattern when:

* The method is called infrequently or only once.
* The logic is simple and the performance gain would be negligible.
* You're working in a context where clarity or readability is more important than micro-optimization.

## How It Works

Instead of repeatedly calling `obj.method()`, you assign the method to a local variable once:

```python
method = obj.method
```

Now you can call `method()` directly, avoiding the overhead of repeated attribute access.

This works because in Python, methods are objects too, and accessing a bound method returns a callable that includes both the function and its associated object (`self`).

## Real-World Analogy

Imagine you're a librarian looking up a specific book title thousands of times. Rather than going to the shelf and scanning every row repeatedly, you write the book’s location on a sticky note once. Then you use the note to go straight to the book every time—that’s what prebinding does for method calls.

## Simplified Example

```python
class Processor:
    def process_text(self, text):
        print(f"Processing text: {text}")

proc = Processor()

# Prebind the method
process_text = proc.process_text

# Use it repeatedly
for _ in range(3):
    process_text("Hello, world!")
```

This avoids repeating the `proc.process_text` lookup each time through the loop.

## Learn More

You can view a full implementation of this pattern here:
[Prebound Method Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/prebound_method.py)
