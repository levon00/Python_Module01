#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = float(height)
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
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def get_growth(self) -> float:
        return self._growth


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    plant = Plant("Sunflower", 25, 45)
    plant.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.age()
        plant.grow()
        plant.show()
    print(f"Growth this week: {7 * plant.get_growth()}cm")
