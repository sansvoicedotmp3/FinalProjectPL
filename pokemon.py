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
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._speed = speed
    
class GenOnePokemon(GenericPokemon):
    def __init__(self, name: str, type:Type, hp:int, attack:int, defense:int, special:int, speed:int):
        super().__init__(name, type, hp, attack, defense, speed)
        self._special = special
        
        #Placeholder for full system

        self.dv = 0 #{"hp": 0, "attack": 0, "defense": 0, "special": 0, "speed": 0}
        self.statexp = 0 #{"hp": 0, "attack": 0, "defense": 0, "special": 0, "speed": 0}

    def get_real_hp(self, level = 100) -> int:
        return int(math.floor((((((self._hp + self.dv ) * 2) + (math.sqrt(self.statexp) / 4))* level) / 100)) + level + 10)
    
    def get_real_attack(self, level = 100) -> int:
        return int(math.floor((((((self._attack + self.dv ) * 2) + (math.sqrt(self.statexp) / 4))* level) / 100)) + 5)
    
    def get_real_defense(self, level = 100) -> int:
        return int(math.floor((((((self._defense + self.dv ) * 2) + (math.sqrt(self.statexp) / 4))* level) / 100)) + 5)
    
    def get_real_special(self, level = 100) -> int:
        return int(math.floor((((((self._special + self.dv ) * 2) + (math.sqrt(self.statexp) / 4))* level) / 100)) + 5)
    
    def get_real_speed(self, level = 100) -> int:
        return int(math.floor((((((self._speed + self.dv ) * 2) + (math.sqrt(self.statexp) / 4))* level) / 100)) + 5)

class GenThreePokemon(GenericPokemon):
    def __init__(self, name:str, type:Type, hp:int, attack:int, defense:int, special_attack:int, special_defense:int, speed:int):
        super().__init__(name, type, hp, attack, defense, speed)
        self._special_attack = special_attack
        self._special_defense = special_defense

        #Placeholder for full system
        self.iv = 0 #{"hp": 0, "attack": 0, "defense": 0, "special_attack": 0, "special_defense": 0, "speed": 0}
        self.ev = 0 #{"hp": 0, "attack": 0, "defense": 0, "special_attack": 0, "special_defense": 0, "speed": 0}

    def get_real_hp(self, level = 100) -> int:
        return int(math.floor((((((self._hp) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + level + 10)
    
    def get_real_attack(self, level = 100) -> int:
        return int(math.floor((((((self._attack) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + 5)
    
    def get_real_defense(self, level = 100) -> int:
        return int(math.floor((((((self._defense) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + 5)
    
    def get_real_special_attack(self, level = 100) -> int:
        return int(math.floor((((((self._special_attack) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + 5)
    
    def get_real_special_defense(self, level = 100) -> int:
        return int(math.floor((((((self._special_defense) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + 5)
    
    def get_real_speed(self, level = 100) -> int:
        return int(math.floor((((((self._speed) * 2) + self.iv + math.floor((self.ev / 4)))* level) / 100)) + 5)