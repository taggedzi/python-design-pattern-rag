# The Interpreter Pattern (Behavioral)

## Purpose

The Interpreter pattern defines a way to evaluate expressions in a language using a class-based structure. It’s useful when you have a language or set of rules to interpret, and the grammar is simple enough to model using classes and methods.

## The Problem It Solves

When your program needs to evaluate expressions or commands written in a specific syntax (like a mini-language), the logic can become messy and hard to maintain. The Interpreter pattern helps organize this logic by turning parts of the language into objects that can interpret themselves.

## When to Use It

This pattern is useful when:

* You need to evaluate structured expressions or rules (like math formulas or logical statements).
* You’re building a domain-specific language (DSL).
* You want to write a simple interpreter without using external parser tools.
* Performance isn't critical, and clarity or flexibility is more important.

## When NOT to Use It

Avoid this pattern if:

* The grammar is complex or changes frequently—this can make the code difficult to manage.
* You need high performance—interpreting with objects can be slower than other methods.
* You're only evaluating very simple expressions that don’t require an abstract grammar.

## How It Works

The pattern involves the following components:

1. **Context** – Stores data like variable values (e.g., `{"x": 10, "y": 5}`).
2. **Terminal Expressions** – Basic elements of the language (e.g., variables or constants).
3. **Non-Terminal Expressions** – Combine terminal expressions to form larger structures (e.g., addition, subtraction).
4. **Abstract Syntax Tree (AST)** – Represents the full expression.
5. Each class includes an `interpret()` method to evaluate itself using the context.

## Real-World Analogy

Imagine you're a librarian with books organized in a standard way. Even if you don’t know the details of each book, you can still find specific information using the consistent format. The Interpreter pattern works similarly by applying a fixed structure to evaluate different expressions.

## Simplified Example

Here's a basic example in Python:

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
* The `interpret()` method calculates the result based on the values in the context.

## Learn More

For the complete Python implementation, visit:
[interpreter.py on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/interpreter.py)
