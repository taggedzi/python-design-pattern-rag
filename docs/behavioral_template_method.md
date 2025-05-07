# The Template Method Pattern (Behavioral)

## Intent
The Template Method pattern provides a way to define an algorithm's skeleton, deferring some steps of the algorithm to subclasses. It lets one redefine certain steps of an algorithm without changing its structure.

## Problem It Solves
It addresses the problem of designing algorithms by encapsulating the invariant parts and leaving only the variable or extensible parts to be implemented by subclasses. This separation allows for code reuse, flexibility, and maintainability in software development.

## When to Use It
The Template Method pattern is beneficial when you have a complex algorithm that has multiple steps, some of which are common among all algorithms but can vary based on the specifics of each subclass. 

For instance, if you're implementing different types of documents like reports or letters, and they share a basic structure (like header, body, footer), while the content within these structures might differ. In such cases, using the Template Method pattern can help to encapsulate this common structure into a superclass and let subclasses fill in the specifics.

## When NOT to Use It
The Template Method is not suitable for simple algorithms or when each step needs to be implemented differently based on different conditions. 

## How It Works
The Template Method pattern involves an abstract base class (AbstractClass) that defines a template method (template_method). This template method contains the algorithm's steps, with certain steps left as abstract methods for subclasses to implement (required_operations_1, required_operations_2). Optionally, it also includes hook methods (hook_1 and hook_2), which can be overridden by subclasses but are not mandatory. 

The concrete subclasses (ConcreteClassA and ConcreteClassB) then provide the implementation for these abstract methods to carry out the specific steps of their respective algorithms.

## Real-World Analogy
Imagine a recipe for a dish. The template method would be the entire process, including how many ingredients are used, what order they should be put in, and any common cooking steps like boiling water or mixing ingredients. Variations could be different types of pasta dishes (ConcreteClassA) or spaghetti bolognese (ConcreteClassB), each with their own specific methods to add the sauce or seasoning.

## Simplified Example
The provided Python code is a simplified example of the Template Method pattern:

```python
class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation_1()
        self.required_operations_1()
        self.base_operation_2()
        self.hook_1()
        self.required_operations_2()
        self.hook_2()
    # ...

class ConcreteClassA(AbstractClass):
    def required_operations_1(self) -> None:
        print("ConcreteClassA: Implemented required_operation_1")
    # ...
```

## See Also
You can find the full Python code for this pattern in the [Python file](https://github.com/username/repo-name/blob/main/python_design_patterns/behavioral/template_method.py) in our GitHub repository.