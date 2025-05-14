# The Three-Tier Pattern (Structural)

## Purpose

The Three-Tier pattern divides an application into three distinct layers: data, logic, and presentation. This structure helps keep code organized, easier to maintain, and more scalable as the application grows.

## Problem It Solves

In many applications, data handling, business logic, and user interfaces are mixed together. This can make the code hard to manage, test, or update. The Three-Tier pattern solves this by assigning each responsibility to its own layer, allowing you to change one part without affecting the others.

## When to Use It

Use this pattern when:

* Your application includes both user interaction and data storage.
* You want to separate the business logic from the interface.
* You need a maintainable, testable structure for a growing codebase.

## When Not to Use It

Avoid this pattern if:

* The app is small, with little or no business logic.
* Adding structure would make the design unnecessarily complex.
* You don’t expect the app to scale or grow in functionality.

## How It Works

The application is divided into three layers:

1. **Data Layer** – Manages data storage and retrieval (e.g., databases or files).
2. **Logic Layer** – Handles rules, processing, and decision-making.
3. **Presentation Layer** – Manages how users interact with the app (e.g., UI or command-line interface).

Each layer communicates only with its neighboring layer, promoting clean separation of responsibilities.

## Real-World Analogy

Think of a restaurant:

* The **kitchen** (Data Layer) prepares the food.
* The **chef** (Logic Layer) decides how to prepare the food based on the order.
* The **waiter** (Presentation Layer) takes orders from customers and delivers food.

Each part does its job without needing full knowledge of the others.

## Simplified Example

Here’s a basic example in Python:

```python
# Data Layer
_data = []

def save(item):
    _data.append(item)

def fetch():
    return list(_data)

# Logic Layer
def add(item):
    if item:
        save(item)
    else:
        raise ValueError("Item cannot be empty.")

def get_all():
    return fetch()

# Presentation Layer
while True:
    print("\n=== Menu ===")
    print("1. Add Item")
    print("2. View Items")
    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter the item: ")
        try:
            add(item)
            print("Item added.")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "2":
        items = get_all()
        if not items:
            print("No items found.")
        else:
            for i, item in enumerate(items, 1):
                print(f"{i}. {item}")
```

This example separates storage, processing, and user interaction into three simple layers, each with a single responsibility.

## Learn More

View the full implementation in Python here:
[Three-Tier Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/three_tier.py)
