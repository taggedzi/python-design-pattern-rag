# The Interpreter Pattern (Behavioral)

## Purpose

The Interpreter pattern provides a way to evaluate expressions using a class-based structure. It’s useful for defining and processing a simple language or rule set using code.

## Problem It Solves

When a program needs to evaluate expressions written in a custom syntax—like a small language or set of rules—the logic can get messy. The Interpreter pattern helps by turning each part of the language into a class that knows how to interpret itself, keeping the code organized and easier to manage.

## When to Use It

Use this pattern when:

* You need to evaluate structured expressions (e.g., math or logic).
* You're building a domain-specific language (DSL).
* You want to write an interpreter without relying on external parsing tools.
* Clarity and flexibility are more important than performance.

## When Not to Use It

Avoid this pattern if:

* The grammar is large or changes often.
* You need high performance—this pattern can be slower than other methods.
* You're only working with very simple expressions that don’t require a structured approach.

## How It Works

Key parts of the pattern include:

1. **Context** – Holds variable values (e.g., `{"x": 10, "y": 5}`).
2. **Terminal Expressions** – Simple elements like variables or constants.
3. **Non-Terminal Expressions** – Combine terminal expressions (e.g., addition or subtraction).
4. **Abstract Syntax Tree (AST)** – A tree structure built from terminal and non-terminal expressions.
5. Each class has an `interpret()` method that evaluates the expression using the context.

## Real-World Analogy

Think of a librarian using a library system. Even without knowing each book’s contents, the librarian can find information using a consistent system. Similarly, the Interpreter pattern uses a fixed structure to evaluate various expressions.

## Simplified Example

Here's a basic Python example:

```python
# Context stores variable values
context = Context({"x": 10, "y": 5, "z": 2})

# Build an expression: x + (y - z)
expr = Add(Variable("x"), Subtract(Variable("y"), Variable("z")))

# Interpret and evaluate the expression
print("Result:", expr.interpret(context))  # Outputs: 13
```

In this example:

* `Variable("x")` is a terminal expression.
* `Add()` and `Subtract()` are non-terminal expressions.
* `interpret()` evaluates the full expression using the values in the context.

## Learn More

See a full implementation on GitHub:
[interpreter.py on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/interpreter.py)
