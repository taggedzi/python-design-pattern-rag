# The Facade Pattern (Structural)

## Purpose

The Facade pattern provides a simple, unified interface to a larger and more complex system of classes. It hides the internal details of how the system works, making it easier for users to interact with.

## The Problem It Solves

In many software systems, the inner workings involve multiple classes or APIs that need to be used together correctly. This can make the system hard to understand and use. The Facade pattern addresses this by wrapping the complexity behind a cleaner, higher-level interface. It simplifies usage and reduces the need for users to understand the full structure of the system.

## When to Use It

Use the Facade pattern when:

* You have a complex subsystem with many components or classes.
* You want to provide an easier or more consistent interface for clients.
* You want to separate the implementation of a system from its usage, making it easier to maintain or refactor.

## When NOT to Use It

Avoid using the Facade pattern if:

* Clients need full access to every feature of the subsystem.
* The subsystem is simple and doesn’t benefit from abstraction.
* You don’t want to introduce an extra layer that might become outdated or tightly coupled to the subsystem.

## How It Works

The Facade pattern creates a wrapper class (the facade) that delegates tasks to the right classes in the subsystem. The client interacts only with the facade, not with the individual classes. This makes the system easier to use and reduces dependencies between components.

## Real-World Analogy

Think of a restaurant menu. Instead of asking the chef how to cook each dish, you choose from a menu. The kitchen handles the rest. You don’t need to know how everything works behind the scenes—just what you want to order. That’s what a facade does in software.

## Simplified Example

Imagine a text editor system with two subsystems: one for text files and one for word documents.

```python
class TextFile:
    def open(self, filename):
        print(f"Opening {filename}")
    
    def read(self):
        return "Reading text file content"
    
    def save(self):
        print("Saving text file")

class WordDocument:
    def new_document(self):
        print("Creating new Word document")
    
    def add_text(self, text):
        print(f"Adding text: {text}")
    
    def save_as(self, filename):
        print(f"Saving Word document as {filename}")
```

The facade simplifies access to both:

```python
class TextEditorFacade:
    def __init__(self):
        self.text_file = TextFile()
        self.word_doc = WordDocument()
    
    def new_document(self, text):
        self.word_doc.new_document()
        self.word_doc.add_text(text)
        self.word_doc.save_as("new_doc.docx")
    
    def open_and_read(self, filename):
        self.text_file.open(filename)
        return self.text_file.read()
```

### Usage

```python
editor = TextEditorFacade()
editor.new_document("Hello, world!")
print(editor.open_and_read("file.txt"))
```

This approach simplifies how a developer interacts with the system, hiding unnecessary details.

## Learn More

For the full Python implementation, visit:
[Facade Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/facade.py)
