# The Lazy Evaluation Pattern (Creational)

## Purpose

Lazy Evaluation delays the computation of a value until it’s actually needed. This helps improve performance and reduce memory usage, especially for expensive or rarely used calculations.

## Problem It Solves

Programs often compute values upfront—even if they’re never used. This wastes time and resources. Lazy Evaluation solves this by postponing the computation until the value is first accessed. Once calculated, the result is stored (cached) and reused.

## When to Use It

Use Lazy Evaluation when:

* A value might not be used.
* A calculation is resource-intensive (e.g., time-consuming or memory-heavy).
* You want to improve efficiency by computing only what’s necessary.

Typical use cases include generating reports, analyzing large datasets, or evaluating configuration options that might not be needed.

## When Not to Use It

Avoid this pattern if:

* The value is always needed right away.
* The computation is simple and doesn't benefit from deferral.
* You're in a multi-threaded environment and need thread-safe lazy loading (this example isn’t thread-safe).

## How It Works

A method marked with a decorator like `@lazy_property` runs only the first time it’s accessed. Its result is saved, and future accesses return the cached result instead of recalculating.

## Real-World Analogy

Imagine a pop-up book. A page only reveals its details when opened. If you never open a page, the pop-up remains hidden. Lazy Evaluation works the same way—work is only done when it’s needed.

## Simplified Example

Here’s a simple Python implementation:

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
        time.sleep(2)  # Simulate a costly calculation
        return {
            "total": len(self.data),
            "min": min(self.data),
            "max": max(self.data),
            "average": sum(self.data) / len(self.data)
        }
```

### Usage

```python
report = ReportGenerator([1, 2, 3, 4, 5])

print("First access:")
print(report.summary)  # Triggers computation

print("\nSecond access:")
print(report.summary)  # Returns cached result
```

### Output

```
First access:
Computing 'summary'...
{'total': 5, 'min': 1, 'max': 5, 'average': 3.0}

Second access:
{'total': 5, 'min': 1, 'max': 5, 'average': 3.0}
```

## Learn More

View the full implementation in Python here:
[Lazy Evaluation on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/creational/lazy_evaluation.py)
