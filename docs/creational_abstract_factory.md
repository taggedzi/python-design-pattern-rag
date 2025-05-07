---
file: creational/abstract_factory.py
chunk: creational_abstract_factory.md
---

```python
"""
Creational Pattern: Abstract Factory

Provides an interface for creating families of related or dependent objects
without specifying their concrete classes.
"""

from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

# Concrete Products - Windows
class WindowsButton(Button):
    def render(self) -> str:
        return "Render a Windows-style button."

class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Render a Windows-style checkbox."

# Concrete Products - MacOS
class MacButton(Button):
    def render(self) -> str:
        return "Render a Mac-style button."

class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "Render a Mac-style checkbox."

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Client Code
class Application:
    def __init__(self, factory: GUIFactory) -> None:
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render(self) -> None:
        print(self.button.render())
        print(self.checkbox.render())

# Example usage
if __name__ == "__main__":
    os_type = "mac"  # could also be "windows"

    factory: GUIFactory
    if os_type == "windows":
        factory = WindowsFactory()
    else:
        factory = MacFactory()

    app = Application(factory)
    app.render()

```

## Summary
Abstract Factory pattern implementation in Python for creating GUI components.

## Docstrings
- Creates a family of related or dependent objects without specifying their concrete classes.
- Interface for creating families of related or dependent objects.
- Abstract Product: Interface for rendering GUI elements.
- Concrete Product: Windows-style button.
- Concrete Product: Windows-style checkbox.
- Concrete Product: Mac-style button.
- Concrete Product: Mac-style checkbox.
- Abstract Factory: Interface for creating GUI components.
- Concrete Factory: Creates Windows GUI components.
- Concrete Factory: Creates Mac GUI components.
- Client code: Application class that uses a factory to create GUI components and render them.

