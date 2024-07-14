## Kaden Bilyeu
## 2024-07-14
## Midterm; Question 6
## CS 3080-001
## 6.py

## Testing and debugging here, final answers will be handwritten on the exam.

## Use the following module to complete the question:
## https://www.geeksforgeeks.org/random-numbers-in-python/
## https://pythonspot.com/random-numbers/

## You are a game designer now. You are tasked with making a very basic battle system much like
## pokemon. For this program, the pokemon have two stats: hit points and attack damage. You
## have one pokemon represent you, and one represent the computer. They are to fight it out like
## in the pokemon game, however they will only attack each other. The damage dealt is based on
## the attack damage statistic you created, with the damage being from 1 to the attack damage
## max. Have the pokemon fight it out, whoever reaches 0 hitpoints first loses. Display who won
## the fight. Feel free to use floats or ints.

## built-in libraries
import random

class Pokemon:

    def __init__(self, 
                 name:str, 
                 hit_points:int, 
                 attack_damage:int):
        
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = attack_damage

    def attack(self, 
               other:'Pokemon'):
        
        damage = random.randint(1, self.attack_damage)
        other.hit_points -= damage

        print(f"{self.name} attacks {other.name} for {damage} damage. {other.name} now has {other.hit_points} HP")

player_pokemon = Pokemon("Player", 50, 10)
computer_pokemon = Pokemon("'AI'", 50, 10)

while(player_pokemon.hit_points > 0 and computer_pokemon.hit_points > 0):
    player_pokemon.attack(computer_pokemon)
    
    if(computer_pokemon.hit_points <= 0):
        print(player_pokemon.name + " wins!")
        break
    
    computer_pokemon.attack(player_pokemon)
    
    if(player_pokemon.hit_points <= 0):
        print(computer_pokemon.name + " wins!")

