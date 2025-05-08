---
file: structural/global_object.py
chunk: structural_global_object.md
---

```python
"""
Global Object Pattern Example

This pattern exposes a globally shared object (singleton-like) through module-level
declaration. It provides centralized access to application-wide state or configuration
without enforcing a strict Singleton structure.

Used for: shared config, feature toggles, session state, or dependency registry.

Pattern Type: Structural
"""

# config.py
class AppConfig:
    """
    AppConfig is a shared global object used to store application settings.
    """
    def __init__(self):
        self.environment = "development"
        self.debug_mode = False
        self.api_key = None

# This global instance is what other modules will import
global_config = AppConfig()

# service.py
def initialize_service():
    from config import global_config
    print(f"[Service] Running in {global_config.environment} mode.")
    if global_config.debug_mode:
        print("[Service] Debug mode is enabled.")

def update_api_key(new_key: str):
    from config import global_config
    global_config.api_key = new_key
    print(f"[Service] Updated API key to: {global_config.api_key}")

# main.py
def main():
    from config import global_config
    import service

    # Configure shared state
    global_config.environment = "production"
    global_config.debug_mode = True

    # Service modules use the shared object
    service.initialize_service()
    service.update_api_key("SECRET-123")

    # Show that the global object retains the update
    print(f"[Main] Confirmed API key: {global_config.api_key}")

if __name__ == "__main__":
    main()

```

## Summary
This code demonstrates the Global Object Pattern, showcasing a shared configuration object accessible across modules.

## Docstrings
- AppConfig is a shared global object used to store application settings.
- initialize_service initializes the service and prints the current environment mode.
- update_api_key updates the API key in the global configuration object.

