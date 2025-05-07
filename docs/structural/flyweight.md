# The Flyweight Pattern (Structural)

## Intent
The Flyweight pattern is a memory optimization technique used to minimize memory usage or computational expenses by sharing as much data as possible with similar objects. It's primarily useful when there are many individual objects that are relatively expensive to create and/or require large amounts of storage space.

## Problem It Solves
This pattern addresses the problem of over-reliance on object identity, leading to inefficiencies due to excessive memory usage or computational expense. 

## When to Use It
The Flyweight pattern is particularly effective when there are many individual objects that share a lot of state with similar objects. This can be seen in scenarios where the majority of an application's objects have common properties, such as text editor applications showing multiple documents with shared font styles or graphics rendering systems sharing graphical elements like images.

## When NOT to Use It
Misuse of Flyweight pattern can lead to unnecessary complexity and it should not be used when:
1. The object state is small and does not change often, meaning the objects are rarely updated.
2. If the application needs to maintain a lot of individual objects with different states.
3. When you need to create many instances of an object at runtime.

## How It Works
The Flyweight pattern involves creating shared flyweights for common or repeated states and using them in place of full objects, thereby reducing memory usage. The `Flyweight` class contains the intrinsic (shared) state that's independent of any context, while the `FlyweightFactory` manages these shared flyweights by providing a way to fetch existing ones when needed or creating new ones if none exist yet.

## Real-World Analogy
Imagine you have a large collection of postcards with different addresses and messages on them. If most of the postcards are for the same city, they could share the same physical postcard (the Flyweight). Instead of having a new postcard each time, you can reuse an existing one and just change the message or address. This is similar to how the Flyweight pattern lets us use shared objects without wasting memory on duplicates.

## Simplified Example
Here's a simplified example:
```python
class CarFlyweight:  # The shared Flyweight object containing intrinsic (shared) state.
    def __init__(self, car_type):
        self._car_type = car_type

    def operation(self, license_plate):
        print(f"Car type: {self._car_type} | License plate: {license_plate}")

class CarFlyweightFactory:  # Manages and reuses flyweight instances.
    _flyweights = {}

    def get_flyweight(self, car_type):
        if not self._flyweights.get(car_type):
            print("Creating new flyweight for ", car_type)
            self._flyweights[car_type] = CarFlyweight(car_type)
        else:
            print("Reusing existing flyweight for ", car_type)
        return self._flyweights[car_type]
    
    def list_flyweights(self):
        print("Cars in the Flyweight Factory:")
        for key in self._flyweights.keys():
            print(key, end="\n")

# Example usage
factory = CarFlyweightFactory()
car1 = factory.get_flyweight('Sedan')
car1.operation('ABC-123')  # Shared state: 'Sedan' | Unique state: 'ABC-123'
car2 = factory.get_flyweight('SUV')
car2.operation('XYZ-999')  # Shared state: 'SUV' | Unique state: 'XYZ-999'
factory.list_flyweights()  # Prints: Sedan, SUV
```
## See Also
The Flyweight pattern is a part of the Gang of Four design patterns and can be found in many programming language implementations. The code provided here is an example from Python. It's used as a teaching tool for beginners to understand how this design pattern works and when it could be usefully applied.