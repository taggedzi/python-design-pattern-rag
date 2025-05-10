# The Global Object Pattern (Structural)

## Purpose

The Global Object pattern provides a simple way to share data—such as configuration settings or environment information—across different parts of an application. Unlike the Singleton pattern, it doesn’t enforce that only one instance exists but instead makes a shared instance easily accessible.

## The Problem It Solves

In large applications, it can be difficult to manage shared settings like debug mode, API keys, or environment flags. Passing these values around through every function or class creates clutter. The Global Object pattern solves this by storing shared state in one central place, which any part of the application can access directly.

## When to Use It

Use this pattern when:

* You need to share config or global settings across multiple modules.
* The settings don’t change often during runtime.
* You want a lightweight alternative to Singleton or dependency injection.

Typical examples include debug flags, environment modes (`"development"`, `"production"`), API tokens, feature toggles, and other app-wide variables.

## When NOT to Use It

Avoid using this pattern when:

* Your app is small, and passing data explicitly is simpler and clearer.
* You need strict control over object creation (use Singleton instead).
* You want to avoid tight coupling or make unit testing easier.

Too much reliance on global state can make testing harder and the flow of data harder to follow.

## How It Works

You define a module-level object (usually in a separate file like `config.py`) and import it wherever needed. Since Python modules are cached after their first import, all parts of the application share the same instance of the object.

## Real-World Analogy

Think of a wall-mounted thermostat in a building. Everyone can check it and see the current temperature setting. No one needs to carry around their own copy—it's in a fixed, shared spot. Similarly, the Global Object pattern gives your application one central reference point for shared settings.

## Simplified Example

### `config.py`

```python
class AppConfig:
    def __init__(self):
        self.environment = "development"
        self.debug_mode = False
        self.api_key = None

# This instance is shared throughout the app
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

### Usage

```python
# main.py
from config import global_config
from service import initialize_service

global_config.environment = "production"
global_config.debug_mode = True

initialize_service()
```

### Output

```text
[Service] Running in production mode.
[Service] Debug mode is ON
```

## Learn More

For a full implementation, see:
[Global Object Pattern on GitHub](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/global_object.py)
