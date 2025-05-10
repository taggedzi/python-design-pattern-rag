# The Lazy Evaluation Pattern (Creational)

## Purpose

The Lazy Evaluation pattern delays a calculation until the result is actually needed. This can help improve performance and reduce memory usage, especially when dealing with expensive or unnecessary computations.

## The Problem It Solves

Programs often compute values up front—even if they’re never used. This wastes time and resources. Lazy Evaluation solves this by postponing the computation until the value is specifically requested. Once computed, the result is stored (cached) and reused.

## When to Use It

Use Lazy Evaluation when:

* A value might not always be needed.
* A calculation is expensive (e.g., time-consuming or memory-intensive).
* You want to avoid doing unnecessary work until it becomes necessary.

Common examples include generating reports, processing large datasets, or evaluating settings that may never be accessed.

## When NOT to Use It

Avoid using Lazy Evaluation if:

* The value is always needed immediately.
* The computation is simple and doesn’t benefit from being delayed.
* You need thread safety (this basic example isn’t thread-safe).

## How It Works

Lazy Evaluation typically uses a decorator (like `@lazy_property`) to mark a method for delayed execution. The first time the property is accessed, the method runs, and its result is stored. Future accesses return the cached value without recomputation.

## Real-World Analogy

Think of a pop-up book that reveals a page’s content only when you open it. If you never open a page, the details stay hidden. Similarly, Lazy Evaluation defers the work until it’s needed.

## Simplified Example

Here’s a basic example in Python:

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
        time.sleep(2)  # Simulate an expensive computation
        return {
            "total": len(self.data),
            "min": min(self.data),
            "max": max(self.data),
            "average": sum(self.data) / len(self.data)
        }

# Usage
report = ReportGenerator([1, 2, 3, 4, 5])

print("First access:")
print(report.summary)  # Triggers computation

print("\nSecond access:")
print(report.summary)  # Returns cached result
```

### Output

```text
First access:
Computing 'summary'...
{'total': 5, 'min': 1, 'max': 5, 'average': 3.0}

Second access:
{'total': 5, 'min': 1, 'max': 5, 'average': 3.0}
```

## Learn More

You can find the complete implementation in Python here:
[Lazy Evaluation on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/lazy_evaluation.py)
