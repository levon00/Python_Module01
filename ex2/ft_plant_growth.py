#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age_days: int):
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth = round(height / age_days, 1)
    

    def show(self) -> None:
        save = self.name.capitalize()
        print(f"{save}: {self.height}cm, {self.age_days} days old")
    def age(self) -> None:
        self.age_days += 1
    

    def grow(self) -> None:
        self.height = round(self.height + self.growth, 1)


    def simulate(self) -> None:
        before_height = self.height
        print("=== Garden Plant Growth ===")
        self.show()
        for i in range(1, 8):
            self.grow()
            self.age()
            print(f"=== Day {i} ===")
            self.show()
        print(f"Growth this week: {round(self.height - before_height, 1)}cm")
    

if name == "__main__":
    rose = Plant("Rose", 25, 30)
    rose.simulate()