#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    flowers: list[tuple[str, float, int]] = [
        ("Rose", 25.0, 30),
        ("Sunflower", 80.0, 45),
        ("Cactus", 15.0, 120),
    ]

    for name, height, age in flowers:
        plant = Plant(name, height, age)
        plant.show()
