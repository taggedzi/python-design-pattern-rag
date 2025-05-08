# The Prebound Method Pattern (Structural)

## Intent

The Prebound Method pattern is used to improve performance and decouple method lookup, especially when repeatedly calling object methods within loops or registering callbacks. It allows us to prebind instance methods to local variables for faster execution time.

## Problem It Solves

In Python, the typical way of calling an object's method is through dynamic lookup each iteration in a loop. This can be slow if we have many iterations and/or complex logic inside the method. The Prebound Method pattern solves this by prebinding instance methods to local variables at the start of our program or script, which allows us to call these methods directly without having to do dynamic lookup every time.

## When to Use It

This pattern is beneficial when we have a large number of iterations and complex logic inside an object'<｜begin▁of▁sentence｜> method. We can also use it in scenarios where callbacks are registered with the object frequently or when registering many different types of callbacks at runtime.

## When NOT to Use It

We should not prebind methods if the method is simple, does not contain any complex logic, and we don't need to call it frequently within a loop. Also, if the method needs to be called with specific arguments that are unlikely to change between calls, then prebinding may not provide any performance benefits.

## How It Works

The Prebound Method pattern involves creating local variables for each instance method of an object and assigning these methods to those local variables at the start of our program or script. Then we can call these methods directly using their respective local variable names, without having to do dynamic lookup every time. This is done through Python's descriptor protocol.

## Real-World Analogy

Imagine you are a librarian and have thousands of books in your library. Instead of searching for each book individually (dynamic lookup), you can create an index of all the books at the entrance to the library, so you don't have to search through the entire collection every time you want to find a specific book (prebinding).

## Simplified Example

Here is a simplified example:

```python
class Processor:
    def process_text(self, text):
        print(f"Processing text: {text}")

proc = Processor()
process_text = proc.process_text  # prebinding instance method to local variable
process_text("Hello World")  # calling the method directly using its local variable name
```

## See Also

You can find the full implementation of this pattern in the Python file [Prebound Method Pattern Example](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/prebound_method.py).
