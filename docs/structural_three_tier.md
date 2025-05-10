# The Three-Tier Pattern (Structural)

## Purpose

The Three-Tier pattern organizes an application into three separate layers—data, logic, and presentation. This separation helps keep code clean, easier to maintain, and scalable as the application grows.

## The Problem It Solves

Large or complex applications often mix together data storage, business logic, and user interfaces. This makes the code harder to manage, test, and extend. The Three-Tier pattern addresses this by separating responsibilities into distinct layers that can be developed, tested, and updated independently.

## When to Use It

Use this pattern when:

* Your application has complex logic or a user interface that needs to interact with stored data.
* You want to clearly separate backend logic from the user interface.
* You need to improve maintainability and testability in a growing codebase.

## When NOT to Use It

Avoid this pattern if:

* The application is very simple or has minimal data and logic.
* Adding extra structure would only increase complexity without much benefit.
* You don’t expect the application to grow significantly in size or functionality.

## How It Works

The application is split into three layers:

1. **Data Layer** – Handles storage and retrieval (e.g., databases, files).
2. **Logic Layer** – Processes business rules and decisions.
3. **Presentation Layer** – Manages the user interface and interactions.

Each layer communicates only with its adjacent layer, promoting modularity and clean separation of concerns.

## Real-World Analogy

Think of a restaurant:

* The **kitchen** (Data Layer) prepares the food.
* The **chef** (Logic Layer) decides how to cook the food based on the recipe.
* The **waiter** (Presentation Layer) interacts with customers and brings them their orders.

Each part does its job without needing to know all the details of the others.

## Simplified Example

Here's a basic example in Python:

```python
# Data Layer (in-memory database)
_data = []

def save(item):
    _data.append(item)

def fetch():
    return list(_data)

# Logic Layer (business rules)
def add(item):
    if item:
        save(item)
    else:
        raise ValueError("Item cannot be empty.")

def get_all():
    return fetch()

# Presentation Layer (command-line interface)
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

## Learn More

For the full implementation, see:
[Three-Tier Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/three_tier.py)
