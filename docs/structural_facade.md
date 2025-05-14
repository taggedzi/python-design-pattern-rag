# The Facade Pattern (Structural)

## Purpose

The Facade pattern provides a simple, unified interface to a complex system of classes. It hides internal complexity, making the system easier to use and understand.

## Problem It Solves

Many software systems rely on multiple classes or APIs that must be used together in a specific way. This complexity can make them hard to work with. The Facade pattern solves this by introducing a high-level wrapper class that exposes a cleaner interface, allowing clients to interact with the system without needing to understand or manage its internal details.

## When to Use It

Use this pattern when:

* You want to simplify a system made up of many classes or components.
* You want to provide a clear and consistent interface for clients.
* You need to separate system implementation from how it’s used, helping with maintenance or future changes.

## When Not to Use It

Avoid using the Facade pattern if:

* Clients need full control over or access to the subsystem’s details.
* The subsystem is already simple and adding a facade doesn’t reduce complexity.
* A facade would introduce tight coupling or redundancy.

## How It Works

The Facade pattern introduces a wrapper class that internally manages interactions with multiple components. Clients use only this facade to interact with the system. This reduces the number of dependencies and simplifies the client’s view of the system.

## Real-World Analogy

A restaurant menu is a facade. Diners don’t talk to the chef or learn how to prepare each meal. Instead, they choose from a list, and the kitchen handles everything. The menu hides complexity and simplifies interaction—just like a facade in software.

## Simplified Example

Imagine a system that handles both text files and Word documents:

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

Now, we create a facade to simplify usage:

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

The client code only deals with `TextEditorFacade`, not the individual components, making it easier to use and maintain.

## Learn More

See the full Python implementation here:
[Facade Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/facade.py)
