# The Prototype Pattern (Creational)

## Intent
The prototype pattern is used when creating new objects from existing ones, especially complex ones which require extensive initialization or are time consuming to create. It provides an efficient way to clone objects without coupling implementation details.

## Problem It Solves
This design pattern addresses the problem of object creation in a costly and complex process that requires deep cloning capabilities. 

## When to Use It
The prototype pattern is ideal when:
1. The class to instantiate is expensive or time-consuming to create.
2. A class can't be or shouldn'<｜begin▁of▁sentence｜> not be responsible for knowing how to create its own instances.
3. A class wants to delegate instantiation to run-time, i.e., the client explicity asks for an object and supplies the necessary data.

## When NOT to Use It
1. If a subclass needs to override the clone method. 
2. In cases where the objects are not complex or expensive to create.
3. If you need to maintain different hierarchies of prototypes.

## How It Works
The prototype pattern works by creating an abstract class (Prototype) that provides a clone() interface, and then concrete classes implementing this interface. The Prototype's clone method returns a deep copy of the current object. 

In our example, Shape is a subclass of Prototype which implements the clone() method. It creates a new instance with same color and position as its own but without any reference to it.

## Real-World Analogy
Imagine you have a blue shape at (10,20). You want to create another identical shape at (15,15), instead of creating it from scratch, you can clone the original one and move it to new position. This is how prototype pattern works in real world too.

## Simplified Example
Here's a simplified example:
```python
class Prototype:
    def clone(self): ...  # Returns a deep copy of the current object.
    
class Shape(Prototype):
    def __init__(self, color: str, position: tuple[int, int]):
        self.color = color
        self.position = position
        
    def move(self, dx: int, dy: int): 
        x, y = self.position
        self.position = (x + dx, y + dy)
    
    # other methods...
```
## See Also
[Prototype Python File](https://github.<｜begin▁of▁sentence｜>.com/faif/python-patterns/blob/master/creational/prototype.py)