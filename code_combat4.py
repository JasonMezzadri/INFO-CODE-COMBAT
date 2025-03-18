from random import randint, shuffle, choice

stats = {
    "warrior": {
        "health": (100, 120),
        "shield": (4, 8),
        "energy": (8, 10),
        "attack_dice": "2d6",
        "ability_dice": "1d6"
    },
    "wizard": {
        "health": (70, 90),
        "shield": (3, 5),
        "energy": (14, 18),
        "attack_dice": "1d20",
        "ability_dice": "1d8"
    },
    "rogue": {
        "health": (80, 100),
        "shield": (3, 5),
        "energy": (10, 12),
        "attack_dice": "3d4",
        "ability_dice": "1d4"
    },
    "cleric": {
        "health": (80, 100),
        "shield": (4, 6),
        "energy": (10, 12),
        "attack_dice": "1d12",
        "ability_dice": "1d6"
    }
}


def get_random_player_name():
    names = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr", "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]
    return choice(names)


def get_random_player_surnames():
    surnames = ["Stoneforge", "Moonshadow", "Starwhisper", "Thunderbeard", "Fireheart", "Ravenwing", "Icebane", "Stormrider", "Swiftfoot", "Dragonflame", "Shadowcloak", "Ironhammer", "Frostbeard", "Silverleaf", "Goldenshield", "Windrider", "Hawkseye", "Deepstone", "Steelheart", "Oakenshield"]
    return choice(surnames)

def create_party() -> list[dict]:
    party = [
        create_player("warrior"),
        create_player("wizard"),
        create_player("rogue"),
        create_player("cleric")
    ]
    shuffle(party)
    return party


def get_stats(player_class: str, stat: str) -> int: 
    min_stat, max_stat = stats[player_class][stat]
    return randint(min_stat, max_stat)


def create_player(player_class:str) -> dict:
    player = {
        "name": get_random_player_name(),
        "surname": get_random_player_surnames(),
        "class": player_class,
        "health": get_stats(player_class, "health"),
        "shield": get_stats(player_class, "shield"),
        "energy": get_stats(player_class, "energy"),
        "attack_dice": stats[player_class]["attack_dice"],
        "ability_dice": stats[player_class]["ability_dice"]
    }
    return player

def roll_dice(dice_string: str) -> list[int]:
    parameters = dice_string.split("d")
    number_of_dice = int(parameters[0])
    sides = int(parameters[1])
    dice_list = []
    for _ in range(number_of_dice):
        dice_list.append(randint(1, sides))
    return dice_list

def attack(attacker: dict, defender: dict) -> None:
    attack_dice = roll_dice(attacker["attack_dice"])
    attack_value = sum(attack_dice)
    print(f"{attacker['name']} rolled {attack_value}.")
    print(f"{defender['name']} has {defender['shield']} shield.")
    damage = attack_value - defender['shield']
    if demage < 0:
        demage = 0
        print("The attack missed!")
    print(f"Damage: {damage} ({attack_value} - {defender['shield']})")
    defender[0] -= demage


def get_player_max_health(defensive_team: list[dict]) -> int:
    max_health = -1
    player_index = None
    for i, player in enumerate(defensive_team):
        if player["health"] > max_health:
            max_health = player["health"]
            player_index = i
    return player_index


def get_player_min_health(defensive_team: list[dict]) -> int:
    min_health = 10000
    player_index = None
    for i, player in enumerate(defensive_team):
        if player["health"] < min_health:
            min_health = player["health"]
            player_index = i
    return player_index


def get_player_in_the_middle(defensive_team: list[dict]) -> int:
    return len(defensive_team) // 2


def get_random_edge_player(defensive_team: list[dict]) -> int:
    return choice([0, len (defensive_team) -1])


def choose_defender(attacker_class: str, defensive_team:list[dict]) -> int|None:
    if attacker_class == "warrior":
        return get_player_max_health(defensive_team)
    elif attacker_class == "wizard":
        return get_player_in_the_middle(defensive_team)
    elif attacker_class == "rogue":
        return get_player_min_health(defensive_team)
    elif attacker_class == "cleric":
        return get_random_edge_player(defensive_team)
    else:
        print(f"Class {attacker_class} not recognized. This should never happen!!!")
        return None


def attack_phase(attacking_team: list[dict], defensive_team: list[dict], attacker_index: int) -> None:
    if attacker_index > len(attacking_team) or not defensive_team:
        return None
    
    attacker = attacking_team[attacking_team]
    defender_index = choose_defender(attacker["class"], defensive_team)
    defender = defensive_team[defender_index]
    attack(attacker, defender)

    if defender["health"] <= 0:
        print(f"{defender['name']} has ben defeated.")
        defensive_team.remove(defender)


def combat_phase(party1: list[dict], party2: list[dict]) -> None:
    for i in range(max(len(party1), len(party2))):
        attack_phase(party1, party2, i) # Team 1 attack team 2
        attack_phase(party2, party1, i) # Team 2 attack team 1

def print_party_status(party: list[dict]) -> None:
    pass

def game_loop(party1: list, party2: list) -> None:
    turns = 0
    while party1 and party2:
        print(f"\n [Turn {turns}]")
        combat_phase(party1, party2)
        print("------------")
        print_party_status(party1)
        print_party_status(party2)

        if check_who_won(party1, party2, turns):
            break
        input()


def main():
    party1 = create_party()
    party2 = create_party()
    game_loop(party1, party2)


if __name__ == "__main__":
    main()
