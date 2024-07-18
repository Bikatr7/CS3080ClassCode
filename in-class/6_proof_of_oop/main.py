## Kaden Bilyeu
## 2024-07-17
## In-Class 6: Proof of OOP
## CS 3080-001
## main.py

## I'm doing this without __init__ methods because I am lazy and for this example it is not necessary. Due to the lack of need for initializing instances with different values.
## Output specification is not that specific, so I assume that this would be acceptable. 

##-------------------start-of-Animal--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Animal:

    sound:str | None = None
    food:str | None = None

##-------------------start-of-make_sound()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def make_sound(self:'Animal') -> None:
        if(self.sound):
            print(f"{self.__class__.__name__} says {self.sound}")
        
        else:
            print(f"{self.__class__.__name__} makes no sound")

##-------------------start-of-set_food()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def set_food(self:'Animal', food:str | None) -> None:
        
        self.food = food
        
        if(self.food):
            print(f"{self.__class__.__name__}'s food set to {self.food}")
        else:
            print(f"{self.__class__.__name__} doesn't eat anything")

##-------------------start-of-Dog--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Dog(Animal):
    sound = "woof"
    
##-------------------start-of-Wolf--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Wolf(Dog):
    sound = "howl"

##-------------------start-of-handle_animal_behavior()--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def handle_animal_behavior(animal:Animal, food:str | None) -> None:
    
    animal.make_sound()
    animal.set_food(food)

    if(animal.sound):
        print(f"The {animal.__class__.__name__.lower()} {animal.sound}s and eats {animal.food}")
    else:
        print(f"The {animal.__class__.__name__.lower()} makes no sound and doesn't eat anything")


animal = Animal()
dog = Dog()
wolf = Wolf()

handle_animal_behavior(animal, None)
handle_animal_behavior(dog, "kibble")
handle_animal_behavior(wolf, "meat")