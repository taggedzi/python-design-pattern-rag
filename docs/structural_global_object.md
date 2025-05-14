# The Global Object Pattern (Structural)

## Purpose

The Global Object pattern provides a simple way to share information—like configuration settings or environment flags—across different parts of an application. Unlike the Singleton pattern, it doesn't restrict you to one instance; instead, it offers a shared object that’s easy to access.

## Problem It Solves

Large applications often need shared settings like debug mode, API keys, or environment labels (e.g., `"development"` or `"production"`). Passing these values through every function or class can clutter your code. The Global Object pattern centralizes this shared data in one place, making it accessible without repeated arguments or tightly coupled code.

## When to Use It

Use this pattern when:

* You need to share global settings across multiple modules.
* These settings don’t change frequently at runtime.
* You want a lightweight alternative to Singleton or dependency injection.

Common uses include configuration flags, logging levels, feature toggles, and environment modes.

## When Not to Use It

Avoid using this pattern if:

* Your app is small and simpler with explicitly passed variables.
* You need strict control over object creation (Singleton may be better).
* You want to write highly testable or decoupled code—global objects can make testing harder.

Too much reliance on global state can lead to hidden dependencies and unpredictable behavior in tests.

## How It Works

You define a shared object in a module (like `config.py`) and import it wherever needed. Python ensures that each module is only loaded once, so all imports reference the same instance—effectively making it a shared global.

## Real-World Analogy

Think of a wall-mounted thermostat in a building. Everyone can read the same display to see the temperature setting—no need for every room to have its own. Similarly, a global object offers a shared reference for application-wide data.

## Simplified Example

### `config.py`

```python
class AppConfig:
    def __init__(self):
        self.environment = "development"
        self.debug_mode = False
        self.api_key = None

# Shared instance used across the app
global_config = AppConfig()
```

### `service.py`

```python
from config import global_config

def initialize_service():
    print(f"[Service] Running in {global_config.environment} mode.")
    if global_config.debug_mode:
        print("[Service] Debug mode is ON")
```

### Usage Example (`main.py`)

```python
from config import global_config
from service import initialize_service

global_config.environment = "production"
global_config.debug_mode = True

initialize_service()
```

### Output

```bash
[Service] Running in production mode.
[Service] Debug mode is ON
```

This shows how different modules can access and modify shared settings without tightly coupling them.

## Learn More

View the complete implementation here:
[Global Object Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/global_object.py)
