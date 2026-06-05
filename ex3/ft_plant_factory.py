#!/usr/bin/env python3
class Plant:
    def init(self, name: str, height: float, age_days: int):
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
    

if name == "main":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    print("=== Plant Factory Output ===")
    for i in range(5):
        print("Created: ", end="")
        plants[i].show()
