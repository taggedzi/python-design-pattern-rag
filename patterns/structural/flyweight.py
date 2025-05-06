"""
Structural Pattern: Flyweight

Minimizes memory usage by sharing as much data as possible with similar objects.
Used when many objects share common state that can be externalized.
"""

from typing import Dict

class Flyweight:
    """The shared Flyweight object containing intrinsic (shared) state."""

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        print(f"Flyweight: Shared [{self._shared_state}] | Unique [{unique_state}]")

class FlyweightFactory:
    """Manages and reuses flyweight instances."""

    def __init__(self) -> None:
        self._flyweights: Dict[str, Flyweight] = {}

    def get_flyweight(self, shared_state: str) -> Flyweight:
        if shared_state not in self._flyweights:
            print(f"Factory: Creating new Flyweight for '{shared_state}'")
            self._flyweights[shared_state] = Flyweight(shared_state)
        else:
            print(f"Factory: Reusing existing Flyweight for '{shared_state}'")
        return self._flyweights[shared_state]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"Factory: {count} flyweight(s) in cache:")
        for key in self._flyweights:
            print(f" - {key}")

# Example usage
if __name__ == "__main__":
    factory = FlyweightFactory()

    # Simulate clients with shared car types and unique license plates
    def add_car(factory: FlyweightFactory, car_type: str, plate: str):
        flyweight = factory.get_flyweight(car_type)
        flyweight.operation(plate)

    add_car(factory, "Sedan", "ABC-123")
    add_car(factory, "SUV", "XYZ-999")
    add_car(factory, "Sedan", "DEF-456")

    factory.list_flyweights()
