# The Three Tier Pattern (Structural)

## Intent

The Three-Tier pattern separates an application into three logical tiers or layers. This design provides a clear separation of concerns and makes it easier to manage the development process.

## Problem It Solves

This pattern addresses the issue of making complex applications more maintainable, scalable, and flexible. By dividing an application into separate components that can be developed, tested, deployed, and scaled independently, it provides a better separation of concerns which makes it easier to manage complexity.

## When to Use It

The Three-Tier pattern is ideal for applications with complex business logic or large user bases. It's also beneficial for applications where the frontend and backend are tightly coupled, making them difficult to maintain separately.

## When NOT to Use It

If your application doesn'<｜begin▁of▁sentence｜>t have a lot of business rules that need to be enforced, it might not benefit from using this pattern. If your application is small or simple, it may be overkill to use the Three-Tier pattern.

## How It Works

The three tiers are:

1. Data Layer - Handles data storage and retrieval (like a database).
2. Logic Layer - Applies validation and business rules (the business logic).
3. Presentation Layer - Handles user interaction (like the frontend).

These layers interact with each other, but they don't know about each other except through well-defined interfaces.

## Real-World Analogy

Think of it as a three-tier restaurant: the waiter serves food to customers, the chef prepares and cooks the meal, and the bartender mixes drinks. In this analogy, the waiter is the presentation layer, the chef is the logic layer, and the bartender is the data layer.

## Simplified Example

Here's a simplified example of how it might look:

```python
# Presentation Layer (waiter)
def show_menu():
    print("1. Order food")
    print("2. View menu")

def run_cli():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            # Logic Layer (chef)
            order = get_order()  # interacts with the data layer to fetch the menu and apply business rules
            print(f"Your order: {order}")
            
        elif choice == "2":
            # Data Layer (bartender)
            menu = get_menu()  
            for item in menu:
                print(item)
```

## See Also

You can find the full implementation of this pattern in [three_tier.py](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/three_tier.py).
