#!/usr/bin/env python3
class Plant:
    @staticmethod
    def check_age(age: int) -> None:
        if age >= 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")


    @classmethod
    def create_anonymouse(cls):
        return cls("Unknown Plant", 0, 0)

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        if height < 0:
            self._height = 1
            print("Invalid height value. Height must be a non-negative number.\n")
        else: self._height = height
        if age < 0:
            self._age = 1
            print("Invalid age value. Age must be a non-negative integer.\n")
        else: self._age = age
        if self._age == 0:
            self._growth = 0
        else:
            self._growth = round(self._height / self._age, 1)
        self._grow_times = 0
        self._age_times = 0
        self._show_times = 0


    def show(self) -> None:
        self._show_times += 1
        save = self._name.capitalize()
        print(f"{save}: {self._height}cm, {self._age} days old")

    
    def state(self) -> None:
        print("Current state: ", end="")
        self.show()


    def age(self) -> None:
        self._age += 1
        self._age_times += 1
    

    def grow(self) -> None:
        self._height = round(self._height + self._growth, 1)
        self._grow_times += 1


    def get_name(self) -> str:
        return self._name


    def get_height(self) -> float:
        return round(self._height, 1)


    def get_age(self) -> int:
        return self._age


    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative\nAge update rejected\n")
        else: 
            self._age = age
            print(f"Age updated: {self._age} days")


    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative\nHeight update rejected\n")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm\n")
    
    def state(self) -> None:
        print(f"[statistics for {self._name}]")
        print(f"State {self._grow_times} grow, {self._age_times} age, {self._show_times} show")



class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = False


    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} is not blooming yet.")

    
    def bloom(self) -> None:
        self._blooming = True

    def grow_bloom(self, value: float) -> None:
        print(f"[asking the {self._name} to grow and bloom]")
        self._height += value
        self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self.produce_shade_times = 0
    

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


    def produce_shade(self) -> None:
        self.produce_shade_times += 1
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}\
cm long and {self._trunk_diameter}cm wide.")
    

    def state(self) -> None:
        super().state()
        print(f" {self.produce_shade_times} shade")




class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int,  harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value
def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}\n\
Nutritional value: {self._nutritional_value}")
    
    def grow_and_age(self, value: int) -> None:
        print(f"[make {self._name} grow and age for 20 days]")
        for i in range(value):
            self.grow()
            self.age()
        self._nutritional_value += value 
    

class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds


    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")
        

    def bloom(self) -> None:
        self._blooming = True
        self._seeds += int((self._height + self._age)/2)

    def grow_age_and_bloom(self, value: int) -> None:
        print(f"[make {self._name} grow, age and bloom]")
        for i in range(value):
            self.grow()
            self.age()
        self.bloom()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(800)
    Plant.check_age(3)
    print("\n=== Flower")
    rose = Flower("rose", 30.5, 100, "red")
    rose.show()
    rose.state()
    rose.grow_bloom(10)
    rose.show()
    rose.state()
    print("\n=== Tree")
    oak = Tree("oak", 200.0, 1000, 50.0)
    oak.show()
    oak.state()
    oak.produce_shade()
    oak.state()
    print("\n=== Seed")
    sunflower_seed = Seed("sunflower seed", 0.5, 0, "yellow", 1)
    sunflower_seed.show()
    sunflower_seed.grow_age_and_bloom(20)
    sunflower_seed.show()
    sunflower_seed.state()
    print("\n=== Anonymouse")
    anonymouse = Plant.create_anonymouse()
    anonymouse.show()
    anonymouse.state()