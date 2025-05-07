# The Flyweight Pattern (Structural)

## Intent

Minimizes memory usage by sharing as much data as possible with similar objects. Used when many objects share common state that can be externalized.

## Problem It Solves

It addresses the problem of optimizing an application's performance and resource usage by minimizing the number of objects created, which is especially beneficial in applications dealing with a large number of objects.

## When to Use It

When there are many similar objects that share common state within an application. This pattern can be applied when:
- The program needs to create a large number of objects and this leads to high memory usage or slow performance.
- The object's state is immutable, meaning it doesn’t change after the object is created.

## When NOT to Use It

When the shared state changes frequently or when the objects are meant to be unique (i.e., they have different states). Also, if the program requires a high number of individual objects that don't share much with each other, Flyweight pattern might not be suitable as it reduces memory usage at the cost of increased complexity.

## How It Works

The key classes/functions and their interaction are:
- `Flyweight` class contains shared state (intrinsic state) and has a method for handling unique state.
- `FlyweightFactory` manages flyweights, ensuring that flyweights are reused as much as possible. When a client requests a Flyweight, the Flyweight Factory supplies existing objects if they meet the required criteria; otherwise it creates new ones.

## Real-World Analogy

Think of the Flyweight pattern like a library: books (objects) can be shared among many readers (clients), but each reader has their own unique state (borrowing date, return status etc.). The library is responsible for creating and managing these shared books.

## Simplified Example

```python
class Book:  # Flyweight class
    def __init__(self, title):
        self._title = title

    def borrow(self, user):  # operation with unique state
        print(f"{user} is reading {self._title}")

library = {}  # FlyweightFactory
def get_book(title):
    if title not in library:
        print(f"Adding new book to the library: {title}")
        library[title] = Book(title)
    return library[title]

# Example usage
book1 = get_book("Harry Potter and the Philosopher's Stone")  # Creates a new book
book1.borrow("John Doe")  # Uses an existing book
book2 = get_book("Harry Potter and the Philosopher's Stone")  # Reuses an existing book
book2.borrow("Jane Smith")  # Uses another existing book
```

## See Also

[Flyweight pattern Python file](https://github.<｜begin▁of▁sentence｜>/python-design-patterns/structural/flyweight.py)

This lesson is based on the Flyweight design pattern, which can be found in many textbooks and online resources about software engineering and programming patterns.