# The Three-Tier Pattern (Structural)

## Purpose

The Three-Tier pattern breaks an application into three layers. This helps organize the code, making it easier to build, understand, and update.

## The Problem It Solves

Complex apps can be hard to manage. This pattern helps by dividing the app into smaller parts that can be developed and changed independently. It improves organization, makes testing easier, and helps the app grow over time without becoming too complicated.

## When to Use It

Use this pattern for apps with complex rules or many users. It's helpful when your user interface (frontend) and internal systems (backend) are too connected and hard to manage separately.

## When NOT to Use It

If your app is small or doesn't have many rules, this pattern might be more trouble than it’s worth. In those cases, a simpler design is usually better.

## How It Works

The app is split into three layers:

1. **Data Layer** – Stores and retrieves data (like from a database).
2. **Logic Layer** – Applies rules and handles decisions (business logic).
3. **Presentation Layer** – Shows the interface and handles user input.

Each layer only talks to the one next to it using clear connections, which keeps things organized.

## Real-World Analogy

Think of this pattern like a three-layer brick wall. The bottom layers—the data and logic—are the bricks that give the system its strength and structure. The top layer, the user interface, is like a window built into the wall. It's how you interact with what’s behind the scenes.

## Simplified Example

Here's a simplified example:

```python
# Data Layer (in-memory database)
_data = []

def save(item):
    _data.append(item)

def fetch():
    return list(_data)

# Logic/Business Layer
def add(item):
    if item:
        save(item)
    else:
        raise ValueError("Item cannot be empty.")

def get_all():
    return fetch()

# User Interface Layer (Command Line Interface)
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

## See Also

You can find the full implementation of this pattern in the provided Python file [three_tier.py](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/three_tier.py).
