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
    random_stat = randint(min_stat, max_stat)
    return random_stat


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

def check_who_won():

def combat_phase(party1: list[dict], party2: list[dict]) -> None:
    for i in range(max(len(party1), len(party2))):
        attack_phase(party1, party2) # Team 1 attack team 2
        attack_phase(party2, party1) # Team 2 attack team 1

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
    print(party1)
    print(party2)
    #game_loop(party1, party2)


if __name__ == "__main__":
    main()