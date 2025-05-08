# The Facade Pattern (Structural)

## Intent

The Facade pattern provides a simplified interface to a complex subsystem, such as a set of classes or APIs. It helps decouple clients from the complexity of the subsystem by providing a higher-level interface that does not expose all of its functionality.

## Problem It Solves

In software systems, developers often have to interact with complex subsystems. These subsystems can be hard to understand and use correctly because they may contain many classes or APIs. The Facade pattern provides a simplified interface that hides the complexity of these subsystems from clients. This makes it easier for developers to use the system without having to dive deep into its internals.

## When to Use It

The Facade pattern is useful in situations where you want to provide a simplified interface to a complex subsystem. It's especially beneficial when:

1. You have a large and complex subsystem that contains many classes or APIs.
2. The client code needs to interact with the subsystem, but it shouldn't be aware of its internal complexity.
3. You want to decouple clients from the subsystem's implementation details.

## When NOT to Use It

The Facade pattern should not be used in situations where:

1. The client code needs direct access to all subsystem classes or APIs.
2. The subsystem changes frequently and you want to minimize the impact of these changes on clients.
3. You need to maintain a high level of encapsulation between the facade and its clients.

## How It Works

The Facade class provides a simplified interface that hides the complexity of the underlying subsystem. This is done by delegating calls to methods in the subsystem classes or APIs, which are then executed by the subsystem. The results from these operations are returned to the client code through the facade's interface.

## Real-World Analogy

Imagine a chef who knows how to cook many different dishes but is not an expert in every single detail. Instead of explaining all the steps, he provides you with a menu of options (the Facade) and ensures everything runs smoothly under his watch. If something goes wrong, he can take care of it.

## Simplified Example

Consider a complex subsystem for a text editor:

```python
class TextFile:
    def open(self): pass
    def read(self): pass
    def save(self): pass

class WordDocument:
    def new_document(self): pass
    def add_text(self, text): pass
    def save_as(self, filename): pass
```

A facade could be created to simplify these operations:

```python
class TextEditorFacade:
    def __init__(self):
        self.text_file = TextFile()
        self.word_doc = WordDocument()
    
    def new_document(self, text):
        self.word_doc.new_document()
        self.word_doc.add_text(text)
        
    def open_and_read(self, filename):
        self.text_file.open(filename)
        return self.text_file.read()
```

With this facade, the client code can interact with the text editor in a much simpler way:

```python
editor = TextEditorFacade()
editor.new_document("Hello, world")  # Creates a new Word document with some text
print(editor.open_and_read('file.txt'))  # Opens and reads a text file
```

## See Also

The corresponding Python file for this lesson can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/facade.py)
