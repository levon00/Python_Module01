#!/usr/bin/env python3
class Plant:
    class InternalSystem:
        def __init__(self, plant: "Plant"):
            self._plant = plant
            self._age_calls = 0
            self._grow_calls = 0
            self._show_calls = 0

        def add_age_calls(self) -> None:
            self._age_calls += 1

        def add_grow_calls(self) -> None:
            self._grow_calls += 1

        def add_show_calls(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"[statistics for {self._plant._name}]")
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self._name = name
        if (height < 0):
            print("Height cannot be negative. Setting height to 0.")
            height = 0
        if (age < 0):
            print("Age cannot be negative. Setting age to 0.")
            age = 0
        self._height = height
        self._age = age
        if age == 0:
            self._growth = 0.0
        else:
            self._growth = round(height/age, 1)
        self._internal = Plant.InternalSystem(self)

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        if days <= 365:
            print(f"Is {days} days more than a year? -> False")
            return False
        else:
            print(f"Is {days} days more than a year? -> True")
            return True

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def age(self, days: int = 1) -> None:
        self._internal.add_age_calls()
        self._age += days

    def grow(self, days: int = 1) -> None:
        self._internal.add_grow_calls()
        self._height = round(self._height + round(self._growth * days, 1), 1)

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
        self._internal.add_show_calls()
        print(f"{self._name}: {self._height}cm, "
              f"{self._age} days old")

    def display_statistics(self) -> None:
        self._internal.display()

    def asking(self, text: str) -> None:
        print(f"[asking the {self._name} to {text}]")


class Flower(Plant):
    def __init__(self, name: str, height: float = 0,
                 age: int = 0, color: str = "Unknown"):
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


class Seed(Flower):
    def __init__(self, name: str, height: float = 0,
                 age: int = 0, color: str = "Unknown", seeds: int = 0):
        super().__init__(name, height, age, color)
        self._seeds = seeds
        self._blooming = False

    def bloom(self) -> None:
        super().bloom()
        self._seeds += 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


class Tree(Plant):

    _internal: 'Tree.TreeSystem'

    class TreeSystem(Plant.InternalSystem):
        def __init__(self, plant: "Plant"):
            super().__init__(plant)
            self._produce_shade_calls = 0

        def add_produce_shade(self) -> None:
            self._produce_shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._produce_shade_calls} shade")

    def __init__(self, name: str, height: float = 0,
                 age: int = 0, trunk_diameter: float = 0):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._internal = Tree.TreeSystem(self)

    def show(self) -> None:
        super().show()
        print(f" Trunk Diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        self._internal.add_produce_shade()
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm in wide")


def statistics(plant: "Plant") -> None:
    plant.display_statistics()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.is_older_than_year(30)
    Plant.is_older_than_year(400)
    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "Red")
    rose.show()
    statistics(rose)
    rose.asking("grow and bloom")
    rose.grow(8)
    rose.bloom()
    rose.show()
    statistics(rose)
    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    statistics(oak)
    oak.asking("produce shade")
    oak.produce_shade()
    statistics(oak)
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow", 0)
    sunflower.show()
    sunflower.asking("grow, age and bloom")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    statistics(sunflower)
    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    statistics(unknown)
