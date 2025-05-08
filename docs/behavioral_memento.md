# The Memento Pattern (Behavioral)

## Intent

The Memento pattern is used to restore an object to its previous state, without revealing the details of this implementation to other objects. It provides a way to return to the state before an edit was made.

## Problem It Solves

This design pattern addresses issues related to encapsulation and maintaining history of an object's internal states. This is particularly useful in scenarios where we want to undo operations or implement rollback mechanisms, but without exposing these details to other objects.

## When to Use It

The Memento pattern should be used when:

1. A snapshot of the current state needs to be saved so that it can be restored later.
2. You need to control who has access to this information and how it's stored or transferred.
3. The object's internal state must be preserved, but its class interface should not reveal details about these states.

## When NOT to Use It

The Memento pattern is not suitable when:

1. If the object's state changes frequently, as this would require updating the memento each time.
2. If you need to store and retrieve the mementos across different runs of your program. In such cases, consider using a service or repository that can persist them for you.
3. When the system is unstable and frequent undo/redo operations are required. This could lead to inconsistent states if not handled properly.

## How It Works

The Memento pattern involves three components:

1. `Memento` - stores the internal state of an object and provides access to it.
2. `Originator` - creates a memento containing a snapshot of its current state, and also restores itself from that memento if needed.
3. `Caretaker` - is responsible for keeping the Memento objects but doesn'<｜begin▁of▁sentence｜>t have any information about them. It only knows how to work with Mementos through an interface which all Concrete Memento classes implement.

## Real-World Analogy

Imagine you are a chef who prepares food and takes snapshots of your kitchen at various stages (saving the state). Later, if you need to revert back to that stage, you can simply restore from that snapshot (restoring the state) without knowing how it was prepared. This is similar to how Memento pattern allows an object to be returned to its previous state.

## Simplified Example

Here's a simplified example of how this could look in code:

```python
editor = TextEditor()
history = History()

editor.write("Hello, ")
history.backup(editor.save())  # Save the current state

editor.write("world")
print(editor.get_content())  # Current content: Hello, world

editor.restore(history.undo())  # Restoring to previous state
print(editor.get_content())  # After undo: Hello,  
```

In this example, `TextEditor` is the originator that writes text and saves its current state as a memento in `History` object. Later, it can restore itself from any saved state using the `restore()` method.

## See Also

The Python code for Memento pattern can be found [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/behavioral/observer.py).