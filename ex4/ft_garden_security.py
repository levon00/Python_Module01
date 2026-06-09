#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self._name = name
        if height < 0:
            print("Height cannot be negative. Setting height to 0.")
            height = 0.0
        if age < 0:
            print("Age cannot be negative. Setting age to 0.")
            age = 0
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

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age cannot be negative")
            print("Age update rejected")
        else:
            print(f"Age updated: {self._age} days")
            self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height cannot be negative")
            print("Height update rejected")
        else:
            print(f"Height updated: {self._height}cm")
            self._height = height

    def show(self) -> None:
        print(f"Plant created: {self._name}: {self._height}cm, \
{self._age} days old")

    def state(self) -> None:
        print(f"Current state: {self._name}: {self._height}cm, \
{self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15, 10)
    plant.show()
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    plant.set_age(-10)
    print()
    plant.state()
