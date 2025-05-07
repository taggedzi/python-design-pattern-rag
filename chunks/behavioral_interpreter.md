---
file: behavioral/interpreter.py
chunk: behavioral_interpreter.md
---

```python
"""
Behavioral Pattern: Interpreter

Defines a representation for a grammar and an interpreter that uses the representation
to interpret sentences in the language. Useful for simple language parsing.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict

# Context provides input for interpretation
class Context:
    def __init__(self, variables: Dict[str, int]) -> None:
        self.variables = variables

# Abstract Expression
class Expression(ABC):
    @abstractmethod
    def interpret(self, context: Context) -> int:
        pass

# Terminal Expression
class Variable(Expression):
    def __init__(self, name: str) -> None:
        self.name = name

    def interpret(self, context: Context) -> int:
        return context.variables.get(self.name, 0)

# Non-terminal Expressions
class Add(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self, context: Context) -> int:
        return self.left.interpret(context) + self.right.interpret(context)

class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self, context: Context) -> int:
        return self.left.interpret(context) - self.right.interpret(context)

# Example usage
if __name__ == "__main__":
    context = Context({"x": 10, "y": 5})
    expr = Add(Variable("x"), Subtract(Variable("y"), Variable("z")))  # x + (y - z)
    print("Result:", expr.interpret(context))

```

## Summary
This code defines a simple interpreter for a basic arithmetic language using the Interpreter pattern.

## Docstrings
- Defines a representation for a grammar and an interpreter that uses the representation to interpret sentences in the language. Useful for simple language parsing.
- Context provides input for interpretation
- Abstract Expression
- Terminal Expression
- Non-terminal Expressions
- Example usage

