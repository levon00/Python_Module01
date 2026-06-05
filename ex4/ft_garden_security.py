#!/usr/bin/env python3
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
        print(f"Plant created:", end=" ")
        self.show()
        self._growth = round(self._height / self._age, 1)


    def show(self) -> None:
        save = self._name.capitalize()
        print(f"{save}: {self._height}cm, {self._age} days old\n")

    
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


if __name__ == "__main__":
    print("=== Garden Security Output ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", -200.0, 365)
    plant3 = Plant("Cactus", 5.0, -90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", -15.0, -120)
    plant1.set_age(-10)
    plant1.set_height(-5.0)
    plant1.state()