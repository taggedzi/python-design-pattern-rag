"""
lazy_evaluation.py

Demonstrates the Lazy Evaluation pattern in Python using a custom @lazy_property decorator.
This pattern is useful when you want to delay the evaluation of a resource-intensive
property until it is actually accessed.

"""

import time
from functools import wraps

def lazy_property(func):
    """
    A decorator that converts a method into a lazily evaluated property.
    The result is cached after the first computation.

    Usage:
        @lazy_property
        def expensive_computation(self): ...
    """
    attr_name = f"_lazy_{func.__name__}"

    @property
    @wraps(func)
    def wrapper(self):
        if not hasattr(self, attr_name):
            print(f"🔄 Computing '{func.__name__}'...")
            setattr(self, attr_name, func(self))
        return getattr(self, attr_name)

    return wrapper


# ============================
# Lazy Evaluation Example Class
# ============================

class ReportGenerator:
    """
    Simulates a class that generates an expensive report.
    Lazy evaluation is used so the report is not computed until needed.
    """

    def __init__(self, data: list):
        self.data = data

    @lazy_property
    def summary(self):
        """
        Simulates a time-consuming operation.
        """
        time.sleep(2)  # Simulate heavy computation
        return {
            "total": len(self.data),
            "min": min(self.data),
            "max": max(self.data),
            "average": sum(self.data) / len(self.data)
        }

    def show_summary(self):
        """Displays the report summary."""
        print("📊 Report Summary:")
        for key, value in self.summary.items():
            print(f" - {key.capitalize()}: {value}")


# ============================
# Demonstration
# ============================

def main():
    print("🐢 Lazy Evaluation Pattern Demo 🐢\n")

    numbers = list(range(1, 1_000_001))  # Large dataset
    report = ReportGenerator(numbers)

    print("Step 1: Object created, report not yet generated.")
    time.sleep(1)

    print("\nStep 2: Accessing the summary for the first time (will compute)...")
    report.show_summary()

    print("\nStep 3: Accessing the summary again (should be cached)...")
    report.show_summary()


if __name__ == "__main__":
    main()


# 🐢 Lazy Evaluation Pattern Sample Output 🐢

# Step 1: Object created, report not yet generated.

# Step 2: Accessing the summary for the first time (will compute)...
# 🔄 Computing 'summary'...
# 📊 Report Summary:
#  - Total: 1000000
#  - Min: 1
#  - Max: 1000000
#  - Average: 500000.5

# Step 3: Accessing the summary again (should be cached)...
# 📊 Report Summary:
#  - Total: 1000000
#  - Min: 1
#  - Max: 1000000
#  - Average: 500000.5
