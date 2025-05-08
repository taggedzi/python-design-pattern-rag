# The Global Object Pattern (Structural)

## Intent

The global object pattern is a design pattern that exposes a globally shared object through module-level declaration, providing centralized access to application-wide state or configuration without enforcing a strict Singleton structure. It's often used for sharing config data across the app like environment settings, debug mode status, API keys etc.

## Problem It Solves

The problem this pattern solves is related to managing shared global state in large applications where it can be difficult to manage and maintain due to its complexity. This pattern provides a centralized place to store these configurations that can be accessed from anywhere in the application without having to pass them around as function parameters or through class constructors.

## When to Use It

This pattern is ideal when you have shared configuration data across your app, such as environment settings (production vs development), debug mode status, API keys etc. 

## When NOT to Use It

It's not recommended for small applications where the scope of the application is limited and there are few shared configurations. Also, it can lead to tight coupling in large systems as it makes the code harder to understand and maintain.

## How It Works

The global object pattern works by declaring a shared object at the module level (usually in its own file). This object can be accessed from anywhere within your application without having to pass it around as function parameters or through class constructors. The shared state is typically initialized once when the module is loaded and remains unchanged throughout the execution of the program.

## Real-World Analogy

Imagine a global dictionary in Python that stores all the configuration settings for an app. You can think of this pattern as similar to how a dictionary (or map) might be used in other programming languages, where you have keys and values that are accessible from anywhere within your program.

## Simplified Example

Here's a simplified example:

```python
# config.py
class AppConfig:
    def __init__(self):
        self.environment = "development"
        self.debug_mode = False
        self.api_key = None

global_config = AppConfig()  # This is the shared object

# service.py
def initialize_service():
    from config import global_config
    print(f"[Service] Running in {global_config.environment} mode.")
    if global<｜begin▁of▁sentence｜>:
```

## See Also

You can find the full implementation of this pattern [here](https://github.com/taggedzi/python-design-pattern-rag/blob/main/patterns/structural/global_object.py).