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
            self._age = age
            print(f"Age updated: {self._age} days")
        self._update_growth()

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height cannot be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")
        self._update_growth()

    def _update_growth(self) -> None:
        if self._age == 0:
            self._growth = 0.0
        else:
            self._growth = round(self._height / self._age, 1)

    def show(self) -> None:
        print(f"Plant created: {self._name}: \
{self._height}cm, {self._age} days old")

    def state(self) -> None:
        print(f"Current state: {self._name}: \
{self._height}cm, {self._age} days old")

    def asking(self, text: str) -> None:
        print(f"[asking the {self._name} to {text}]")


class Flower(Plant):
    def __init__(self, name: str, height: float = 0.0,
                 age: int = 0, color: str = "Unknown") -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = False

    def bloom(self) -> None:
        self._blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._blooming:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully")


class Tree(Plant):
    def __init__(self, name: str, height: float = 0.0,
                 age: int = 0, trunk_diameter: int = 0) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk Diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of {self._height}cm "
            f"long and {self._trunk_diameter}cm in wide"
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float = 0.0,
        age: int = 0,
        harvest_season: str = "Unknown",
        nutritional_value: int = 0,
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest Season: {self._harvest_season}\n\
Nutritional Value: {self._nutritional_value}")

    def grow_age(self, days: int) -> None:
        print(f"[make {self._name} grow and age for {days} days]")
        for _ in range(days):
            self.age()
            self.grow()
        self._nutritional_value += days


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    flower.asking("bloom")
    flower.bloom()
    flower.show()
    print("\n=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    tree.asking("produce shade")
    tree.produce_shade()
    print("\n=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable.show()
    vegetable.grow_age(20)
    vegetable.show()
