# The Lazy Evaluation Pattern (Creational)

## Purpose

The Lazy Evaluation pattern delays computing a value until it's actually needed. This is useful when the computation is resource-heavy or time-consuming, like generating a detailed report or performing complex calculations.

## The Problem It Solves

Often, programs compute values upfront—even when those values may never be used. This wastes resources. Lazy Evaluation fixes that by waiting to compute a value until it’s actually requested, which can make programs faster and more efficient.

## When to Use It

Use this pattern when:

* A computation might not always be needed.
* The calculation takes a lot of time or memory.
* You want to improve the performance of your program by avoiding unnecessary work.

An example might be generating a report only when a user opens it—not when the report object is first created.

## When NOT to Use It

Avoid this pattern if:

1. The value is always needed right away.
2. The calculation is simple and quick, and delaying it adds unnecessary complexity.
3. Your application requires thread safety—this basic version of Lazy Evaluation isn’t thread-safe.

## How It Works

The key part is a `@lazy_property` decorator. This turns a method into a property that’s calculated only the first time it’s accessed. After that, the result is stored and reused.

## Real-World Analogy

Imagine reading a book where each chapter appears only when you open it. Instead of loading the whole book at once, each part is created on demand—saving time and effort if you don’t read every chapter.

## Simplified Example

Here’s a basic example with a class that creates a report from a dataset:

```python
import time

def lazy_property(func):
    attr = f"_lazy_{func.__name__}"

    @property
    def wrapper(self):
        if not hasattr(self, attr):
            print(f"Computing '{func.__name__}'...")
            setattr(self, attr, func(self))
        return getattr(self, attr)
    
    return wrapper

class ReportGenerator:
    def __init__(self, data):
        self.data = data

    @lazy_property
    def summary(self):
        time.sleep(2)  # Simulates a slow computation
        return {
            "total": len(self.data),
            "min": min(self.data),
            "max": max(self.data),
            "average": sum(self.data) / len(self.data)
        }

# Demonstration
report = ReportGenerator([1, 2, 3, 4, 5])
print("First access:")
print(report.summary)  # Triggers computation
print("\nSecond access:")
print(report.summary)  # Uses cached result
```

The first time `report.summary` is accessed, it runs the computation and prints the result. The second time, it just returns the stored value—no waiting.

## Learn More

For the full example, see the [lazy_evaluation.py](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/lazy_evaluation.py) file in the repository.
