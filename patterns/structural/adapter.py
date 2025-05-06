"""
Structural Pattern: Adapter

Allows incompatible interfaces to work together by wrapping one interface
and exposing it as another expected by the client.
"""

class Target:
    """The domain-specific interface that clients expect."""

    def request(self) -> str:
        return "Target: The default behavior."

class Adaptee:
    """A class with an incompatible interface."""

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"  # reversed string

class Adapter(Target):
    """
    Adapts the Adaptee to the Target interface.
    Translates the method call and adjusts the data format.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"

# Example usage
if __name__ == "__main__":
    target = Target()
    print(target.request())

    adaptee = Adaptee()
    print("Adaptee:", adaptee.specific_request())

    adapter = Adapter(adaptee)
    print(adapter.request())
