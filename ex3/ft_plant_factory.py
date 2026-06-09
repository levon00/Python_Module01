#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age
        if age == 0:
            self._growth = 0.0
        else:
            self._growth = round(self._height / self._age, 1)

    def age(self) -> None:
        self._age += 1

    def grow(self) -> None:
        self._height = round(self._height + round(self._growth, 1), 1)

    def show(self) -> None:
        print(f"Created: {self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants: list[tuple[str, float, int]] = [
        ("Rose", 25.0, 30),
        ("Oak", 200.0, 365),
        ("Cactus", 5.0, 90),
        ("Sunflower", 80.0, 45),
        ("Fern", 15.0, 120),
    ]

    for name, height, age in plants:
        new_plant = Plant(name, height, age)
        new_plant.show()
