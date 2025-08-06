from dataclasses import dataclass

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

class GenThreePokemon(GenericPokemon):
    def __init__(self, name:str, type:Type, hp:int, attack:int, defense:int, special_attack:int, special_defense:int, speed:int):
        super().__init__(name, type, hp, attack, defense, speed)
        self.special_attack = special_attack
        self.special_defense = special_defense