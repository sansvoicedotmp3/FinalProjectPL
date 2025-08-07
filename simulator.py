import pokemon
import random

# POKEMON AND MOVE SELECTION - HARDCODED

genOneBox = []
genThreeBox = []

movepool = []

genOneBox.append(pokemon.GenOnePokemon("Mew", pokemon.Type("Psychic"), 100, 100, 100, 100, 100))
genOneBox.append(pokemon.GenOnePokemon("Machamp", pokemon.Type("Fighting"), 90, 130, 80, 65, 55))
genOneBox.append(pokemon.GenOnePokemon("Snorlax", pokemon.Type("Normal"), 160, 110, 65, 65, 30))

genThreeBox.append(pokemon.GenThreePokemon("Mew", pokemon.Type("Psychic"), 100, 100, 100, 100, 100, 100))
genThreeBox.append(pokemon.GenThreePokemon("Machamp", pokemon.Type("Fighting"), 90, 130, 80, 65, 85, 55))
genThreeBox.append(pokemon.GenThreePokemon("Snorlax", pokemon.Type("Normal"), 160, 110, 65, 65, 110, 30))

movepool.append(pokemon.Move("Body Slam", "Normal", 85, 100))
movepool.append(pokemon.Move("Psychic", "Psychic", 90, 100))
movepool.append(pokemon.Move("Close Combat", "Fighting", 120, 100))

# UTILITY FUNCTIONS - DEPRECATED

def get_hp(pkmn:pokemon.GenericPokemon, level = 100) -> int:
    return int(((pkmn.hp * 2 * level) / 100) + level + 10)

def get_other_stat(stat:int, level = 100) -> int:
    return int(((stat * 2 * level) / 100) + 5)

# GENERATION 1

def get_damage_g1(move:pokemon.Move, attacker:pokemon.GenOnePokemon, defender:pokemon.GenOnePokemon, attacker_level = 100, defender_level = 100, crit = False) -> int:
    crit_mult = 1
    if crit:
        crit_mult = 2
    stab = 1
    if move.type == attacker.type.type_one or move.type == attacker.type.type_two:
        stab = 1.5
    if move.type in ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost"]:
        base_damage = (((((2*attacker_level*crit_mult)/5) + 2) * move.power * (attacker.get_real_attack() / defender.get_real_defense())) / 50) + 2
    else:
        base_damage = (((((2*attacker_level*crit_mult)/5) + 2) * move.power * (attacker.get_real_special() / defender.get_real_defense())) / 50) + 2
    if defender.type.type_two == None:
        return int(base_damage*crit_mult*stab*get_gen_one_type_effectiveness(move.type, defender.type.type_one))
    else:
        return int(base_damage*crit_mult*stab*get_gen_one_type_effectiveness(move.type, defender.type.type_one)*get_gen_one_type_effectiveness(move.type, defender.type.type_two))

def get_gen_one_type_effectiveness(attacker:str, defender:str) -> float:
    type_chart = {
        "Fire": [["Ice", "Grass", "Bug"],["Fire", "Water", "Rock", "Dragon"]],
        "Water": [["Fire", "Ground", "Rock"],["Water", "Grass", "Dragon"]],
        "Electric": [["Water", "Flying"],["Electric", "Grass", "Ground", "Dragon"]],
        "Grass": [["Water", "Ground", "Rock"],["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon"]],
        "Ice": [["Grass", "Ground", "Flying", "Dragon"],["Water", "Ice"]],
        "Fighting": [["Normal", "Ice", "Rock"],["Poison", "Flying", "Psychic", "Bug", "Ghost"]],
        "Poison": [["Grass", "Bug"],["Poison", "Ground", "Rock", "Ghost"]],
        "Ground": [["Fire", "Electric", "Poison", "Rock"],["Grass", "Bug", "Flying"]],
        "Flying": [["Grass", "Fighting", "Bug"],["Electric", "Rock"]],
        "Psychic": [["Fighting", "Poison"],["Psychic"]],
        "Bug": [["Grass", "Psychic"],["Fire", "Fighting", "Poison", "Flying", "Ghost"]],
        "Rock": [["Fire", "Ice", "Flying", "Bug"],["Fighting", "Ground"]],
        "Ghost": [["Ghost"],["Normal", "Psychic"]],
        "Dragon": [["Dragon"],[]],
        "Normal": [[],["Rock", "Ghost"]]}
    if defender in type_chart[attacker][0]:
        return 2
    elif defender in type_chart[attacker][1]:
        return 0.5
    return 1

# GENERATION 3

def get_damage_g3(move:pokemon.Move, attacker:pokemon.GenThreePokemon, defender:pokemon.GenThreePokemon, attacker_level = 100, defender_level = 100, crit = False) -> int:
    crit_mult = 1
    if crit:
        crit_mult = 2
    stab = 1
    if move.type == attacker.type.type_one or move.type == attacker.type.type_two:
        stab = 1.5
    if move.type in ["Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel"]:
        base_damage = (((((2*attacker_level*crit_mult)/5) + 2) * move.power * (attacker.get_real_attack() / defender.get_real_defense())) / 50) + 2
    else:
        base_damage = (((((2*attacker_level*crit_mult)/5) + 2) * move.power * (attacker.get_real_special_attack() / attacker.get_real_special_defense())) / 50) + 2
    if defender.type.type_two == None:
        return int(base_damage*crit_mult*stab*get_gen_three_type_effectiveness(move.type, defender.type.type_one))
    else:
        return int(base_damage*crit_mult*stab*get_gen_three_type_effectiveness(move.type, defender.type.type_one)*get_gen_three_type_effectiveness(move.type, defender.type.type_two))

def get_gen_three_type_effectiveness(attacker:str, defender:str) -> float:
    type_chart = {
        "Normal": [[], ["Rock", "Ghost"]],
        "Fire": [["Grass", "Ice", "Bug", "Steel"], ["Fire", "Water", "Rock", "Dragon"]],
        "Water": [["Fire", "Ground", "Rock"], ["Water", "Grass", "Dragon"]],
        "Electric": [["Water", "Flying"], ["Electric", "Grass", "Dragon"]],
        "Grass": [["Water", "Ground", "Rock"], ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]],
        "Ice": [["Grass", "Ground", "Flying", "Dragon"], ["Fire", "Water", "Ice", "Steel"]],
        "Fighting": [["Normal", "Ice", "Rock", "Dark", "Steel"], ["Poison", "Flying", "Psychic", "Bug", "Ghost"]],
        "Poison": [["Grass"], ["Poison", "Ground", "Rock", "Ghost"]],
        "Ground": [["Fire", "Electric", "Poison", "Rock", "Steel"], ["Grass", "Bug", "Flying"]],
        "Flying": [["Grass", "Fighting", "Bug"], ["Electric", "Rock", "Steel"]],
        "Psychic": [["Fighting", "Poison"], ["Psychic", "Steel"]],
        "Bug": [["Grass", "Psychic", "Dark"], ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel"]],
        "Rock": [["Fire", "Ice", "Flying", "Bug"], ["Fighting", "Ground", "Steel"]],
        "Ghost": [["Ghost", "Psychic"], ["Normal"]],
        "Dragon": [["Dragon"], ["Steel"]],
        "Dark": [["Psychic", "Ghost"], ["Fighting", "Dark", "Steel"]],
        "Steel": [["Ice", "Rock"], ["Fire", "Water", "Electric", "Steel"]]}
    if defender in type_chart[attacker][0]:
        return 2
    elif defender in type_chart[attacker][1]:
        return 0.5
    return 1

# MAIN FUNCTION HERE

def main():
    print("Hello! Welcome to the Damage Simulator. Which generation would you like to simulate? 1 or 3?")
    gen = 1
    if int(input("Type 1 or 3: ")) != 1:
        gen = 3

    if gen == 1:
        print("Welcome to the gen 1 damage simulator! Please choose your attacking Pokémon from the following!")
        for i in range(len(genOneBox)):
            print(f"{i}: {genOneBox[i].name}")
        attacker = -1
        while attacker < 0 or attacker >= len(genOneBox):
            attacker = int(input("Please enter your choice starting at index 0: "))

        print(f"Excellent! You chose {genOneBox[attacker].name}!")

        print("Please choose your defending Pokémon from the following!")
        for i in range(len(genOneBox)):
            print(f"{i}: {genOneBox[i].name}")
        defender = -1
        while defender < 0 or defender >= len(genOneBox):
            defender = int(input("Please enter your choice starting at index 0: "))

        print("Please choose a move from the movepool:")
        for i in range(len(movepool)):
            move = movepool[i]
            print(f"{i}: {move.name} ({move.type}, Power: {move.power}, Accuracy: {move.accuracy})")
        move_choice = -1
        while move_choice < 0 or move_choice >= len(movepool):
            move_choice = int(input("Enter the move index: "))

        move_used = movepool[move_choice]
        atk:pokemon.GenOnePokemon = genOneBox[attacker]
        dfd:pokemon.GenOnePokemon = genOneBox[defender]

        base_damage = get_damage_g1(move_used, atk, dfd)
        defender_hp = dfd.get_real_hp()

    else:
        print("Welcome to the gen 3 damage simulator! Please choose your attacking Pokémon from the following!")
        for i in range(len(genThreeBox)):
            print(f"{i}: {genThreeBox[i].name}")
        attacker = -1
        while attacker < 0 or attacker >= len(genThreeBox):
            attacker = int(input("Please enter your choice starting at index 0: "))

        print(f"Excellent! You chose {genThreeBox[attacker].name}!")

        print("Please choose your defending Pokémon from the following!")
        for i in range(len(genThreeBox)):
            print(f"{i}: {genThreeBox[i].name}")
        defender = -1
        while defender < 0 or defender >= len(genThreeBox):
            defender = int(input("Please enter your choice starting at index 0: "))

        print("Please choose a move from the movepool:")
        for i in range(len(movepool)):
            move = movepool[i]
            print(f"{i}: {move.name} ({move.type}, Power: {move.power}, Accuracy: {move.accuracy})")
        move_choice = -1
        while move_choice < 0 or move_choice >= len(movepool):
            move_choice = int(input("Enter the move index: "))

        move_used = movepool[move_choice]
        atk:pokemon.GenThreePokemon = genThreeBox[attacker]
        dfd:pokemon.GenThreePokemon = genThreeBox[defender]

        base_damage = get_damage_g3(move_used, atk, dfd)
        defender_hp = dfd.get_real_hp()

    min_damage = int(base_damage * 0.85)
    max_damage = int(base_damage)
    min_percent = round((min_damage / defender_hp) * 100, 2)
    max_percent = round((max_damage / defender_hp) * 100, 2)

    print(f"\n{atk.name} uses {move_used.name} on {dfd.name}!")
    print(f"Damage range: {min_damage} - {max_damage}")
    print(f"That's about {min_percent}% - {max_percent}% of {dfd.name}'s HP.")

if __name__=="__main__":
    main()