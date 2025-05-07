# The Template Method Pattern (Behavioral)

## Intent

The Template Method pattern provides a way to define an algorithm's skeleton, deferring some steps of the algorithm to subclasses. It lets subclasses redefine certain steps of an algorithm without changing its structure.

## Problem It Solves

When we have a complex algorithm that has multiple parts and we want to provide a uniform interface for clients to use it. The problem is that the client should not care about how each part of the algorithm is implemented, but only that it can be used in a consistent way.

## When to Use It

Use this pattern when:
- You have several classes that perform similar tasks and you want to minimize code duplication.
- A class has an algorithm composed of a series of steps, with subclasses providing the implementation for one or more steps. 

## When NOT to Use It

Do not use this pattern if:
- The base class already provides a reasonable default behavior that subclasses should override only when there is a good reason to do so.
- You want to provide hooks into an algorithm at various points, but you don't know in advance what the exact points will be. 

## How It Works

The Template Method pattern defines a skeleton of an algorithm in a superclass but lets subclasses override specific steps without changing the overall algorithm’s structure. The template method calls abstract primitive operations which are implemented by subclasses, hence providing hooks for extension.

## Real-World Analogy

Imagine you're cooking a meal. You define a recipe (the template method) that includes all of the steps to prepare and cook your dish. Then each chef in the kitchen can add their unique twist on how they like to prepare certain ingredients or what seasoning goes best with their favorite type of meat.

## Simplified Example

```python
class AbstractClass:
    def template_method(self):
        self.base_operation_1()
        self.required_operations_1()
        self.base_operation_2()
        self.hook_1()
        self.required_operations_2()
        self.hook_2()
```

## See Also

[TemplateMethodPattern.py](https://github.com/username/repository/blob/main/src/designpatterns/behavioral/template_method/TemplateMethodPattern.py)

This pattern is used in many applications, including GUI frameworks and testing frameworks where you often have a skeleton of an algorithm (the template method) that you want to provide a uniform interface for clients to use.