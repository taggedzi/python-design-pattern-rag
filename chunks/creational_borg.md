---
file: creational/borg.py
chunk: creational_borg.md
---

```python
"""
borg.py

The Borg (Monostate) pattern in Python. This design allows multiple instances of a 
class to share the same state, unlike Singleton which restricts instantiation.
"""

class Borg:
    """
    Borg base class. All instances will share the same internal state (__dict__).
    """
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class AppConfig(Borg):
    """
    Application configuration class using the Borg pattern.

    Any instance of AppConfig will reflect and modify the same shared state.
    """
    def __init__(self):
        super().__init__()
        # Set default only once
        if not hasattr(self, "initialized"):
            self.debug = False
            self.theme = "light"
            self.version = "1.0"
            self.initialized = True

    def set_config(self, debug: bool, theme: str):
        """Update config settings."""
        self.debug = debug
        self.theme = theme

    def show_config(self):
        """Display current configuration."""
        print(f"Debug: {self.debug}, Theme: {self.theme}, Version: {self.version}")


# === Demonstration ===

def main():
    print("🔁 Borg Pattern Demonstration 🔁\n")

    config1 = AppConfig()
    config2 = AppConfig()

    print("Initial State from config1:")
    config1.show_config()

    print("\nUpdating state from config2...")
    config2.set_config(debug=True, theme="dark")

    print("\nState seen from config1 (should reflect changes):")
    config1.show_config()

    print("\nState seen from config2:")
    config2.show_config()

    print(f"\nAre config1 and config2 the same object? {'Yes' if config1 is config2 else 'No'}")
    print(f"Do they share the same state? {'Yes' if config1.__dict__ is config2.__dict__ else 'No'}")


if __name__ == "__main__":
    main()

# Sample Output:
# 🔁 Borg Pattern Demonstration 🔁

# Initial State from config1:
# Debug: False, Theme: light, Version: 1.0

# Updating state from config2...

# State seen from config1 (should reflect changes):
# Debug: True, Theme: dark, Version: 1.0

# State seen from config2:
# Debug: True, Theme: dark, Version: 1.0

# Are config1 and config2 the same object? No
# Do they share the same state? Yes

```

## Summary
Demonstration of the Borg pattern in Python, showcasing shared state across multiple instances.

## Docstrings
- Borg base class. All instances will share the same internal state (__dict__).
- Application configuration class using the Borg pattern. Any instance of AppConfig will reflect and modify the same shared state.
- Update config settings.
- Display current configuration.

