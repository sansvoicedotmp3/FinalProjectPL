from dataclasses import dataclass
import math

@dataclass
class Move:
    name: str
    type: str
    power: int
    accuracy: int = 100

@dataclass
class Type:
    type_one: str
    type_two: str = None

class GenericPokemon:
    def __init__(self, name:str, type:Type, hp:int, attack:int, defense:int, speed:int):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
    
class GenOnePokemon(GenericPokemon):
    def __init__(self, name: str, type:Type, hp:int, attack:int, defense:int, special:int, speed:int):
        super().__init__(name, type, hp, attack, defense, speed)
        self.special = special

        #Placeholder for full system
        self.dv = 0
        self.statexp = 0

    def get_real_hp(self, level = 100) -> int:
        return int(math.floor((((((self.hp + self.dv ) * 2) + (math.sqrt(self.statexp) / 4))* level) / 100)) + level + 10)
    
    def get_real_attack(self, level = 100) -> int:
        return int(math.floor((((((self.attack + self.dv ) * 2) + (math.sqrt(self.statexp) / 4))* level) / 100)) + 5)
    
    def get_real_defense(self, level = 100) -> int:
        return int(math.floor((((((self.defense + self.dv ) * 2) + (math.sqrt(self.statexp) / 4))* level) / 100)) + 5)
    
    def get_real_special(self, level = 100) -> int:
        return int(math.floor((((((self.special + self.dv ) * 2) + (math.sqrt(self.statexp) / 4))* level) / 100)) + 5)
    
    def get_real_speed(self, level = 100) -> int:
        return int(math.floor((((((self.speed + self.dv ) * 2) + (math.sqrt(self.statexp) / 4))* level) / 100)) + 5)

class GenThreePokemon(GenericPokemon):
    def __init__(self, name:str, type:Type, hp:int, attack:int, defense:int, special_attack:int, special_defense:int, speed:int):
        super().__init__(name, type, hp, attack, defense, speed)
        self.special_attack = special_attack
        self.special_defense = special_defense

        #Placeholder for full system
        self.iv = 0
        self.ev = 0

    def get_real_hp(self, level = 100) -> int:
        return int(math.floor((((((self.hp) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + level + 10)
    
    def get_real_attack(self, level = 100) -> int:
        return int(math.floor((((((self.attack) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + 5)
    
    def get_real_defense(self, level = 100) -> int:
        return int(math.floor((((((self.defense) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + 5)
    
    def get_real_special_attack(self, level = 100) -> int:
        return int(math.floor((((((self.special_attack) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + 5)
    
    def get_real_special_defense(self, level = 100) -> int:
        return int(math.floor((((((self.special_defense) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + 5)
    
    def get_real_speed(self, level = 100) -> int:
        return int(math.floor((((((self.speed) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + 5)
    