from itertools import combinations, product
from day21_helpers import parse_boss, parse_shop

def game(player, boss):
    curr_att, curr_def = player.copy(), boss.copy()

    while (curr_att["Hit Points"] > 0) and (curr_def["Hit Points"] > 0):
        damage_dealt = curr_att["Damage"] - curr_def["Armor"]
        damage_dealt = 1 if damage_dealt < 1 else damage_dealt
        curr_def["Hit Points"] -= damage_dealt
        curr_att, curr_def = curr_def, curr_att

    return curr_def["Name"] == player["Name"] # player won


def calc_player_stats(gear):
    player = {stat: 0 for stat in ["Cost", "Damage", "Armor"]}
    for item in flatten(gear):
        for k, v in items_stats[item].items():
            player[k] += v

    player["Hit Points"] = 100
    player["Name"] = "Me"
    return player


def flatten(lst):
    flattened_lst = []
    for item in lst:
        if type(item) == list or type(item) == tuple:
            for subitem in item:
                flattened_lst.append(subitem)
        elif type(item) == str:
            flattened_lst.append(item)
    return flattened_lst


shop = parse_shop("shop.txt")
weapons = list(shop['Weapons'].keys())
armors = list(shop['Armor'].keys())
rings = list(shop['Rings'].keys())

weapon_combinations = weapons # Must carry exactly one weapon
armor_combinations = armors + [None] # Armor in optional
ring_combinations = [] 
for r in [0, 1, 2]: # 0, 1 or 2 rings
    ring_combinations += combinations(rings, r=r)

gear_combinations = product(
        weapon_combinations,
        armor_combinations,
        ring_combinations
        )

items_stats = {**shop['Weapons'], **shop['Armor'], **shop['Rings']}

boss = parse_boss("boss.txt")
min_cost = float("inf")
max_cost = float("-inf")
best_gear = {}
worst_gear = {}
for gear in gear_combinations:
    player = calc_player_stats(gear)
    cost = player['Cost']
    if not (cost < min_cost or cost > max_cost):
        continue
    result = game(player, boss)
    if result and cost < min_cost:
        min_cost = cost
        best_gear = gear
    elif not result and cost > max_cost:
        max_cost = cost
        worst_gear = gear

print(min_cost)
print(best_gear)
print(max_cost)
print(worst_gear)
