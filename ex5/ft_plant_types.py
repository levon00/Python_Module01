class Plant:
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
        self._growth = round(self._height / self._age, 1)


    def show(self) -> None:
        save = self._name.capitalize()
        print(f"{save}: {self._height}cm, {self._age} days old")

    
    def state(self) -> None:
        print("Current state: ", end="")
        self.show()


    def age(self) -> None:
        self._age += 1
    

    def grow(self) -> None:
        self._height = round(self._height + self._growth, 1)


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
            peint(f"Age updated: {self._age} days")


    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative\nHeight update rejected\n")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm\n")


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
            print(" Rose is blooming beautifully!")
        else:
            print(" Rose is not blooming yet.")


    def bloom(self) -> None:
        self._blooming = True
        print("[asking the rose to bloom]")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
    

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(f"Tree Oak now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide.")




class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                age: int,  harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value


    
    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}\n Nutritional value: {self._nutritional_value}")
    
    def grow_and_age(self, value: int) -> None:
        print("[make tomato grow and age for 20 days]")
        for i in range(value):
            self.grow()
            self.age()
        self._nutritional_value += value 
        


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 25, 30, "Red")
    rose.show()
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 50)
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 15, 60, "April", 0)
    tomato.show()
    tomato.grow_and_age(20)
    tomato.show()
