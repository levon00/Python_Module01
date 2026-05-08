#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        save = self.name.capitalize()
        print(f"{save}: {self.height}cm, {self.age} days old\n")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===\n")
    first = Plant("rose", 25, 30)
    first.show()
