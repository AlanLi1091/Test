import numpy as np
import random
import math

rarities = ["R", "SR", "SRLimited", "SRNew", "SSR", "SSRLimited", "SSRNew"]
weight = [float(0.85), float(0.096), float(0.012), float(0.012), float(0.0201), float(0.00495), float(0.00495)]
rarities2 = ["SR", "SRLimited", "SRNew", "SSR", "SSRLimited", "SSRNew"]
weight2 = [float(0.776), float(0.097), float(0.097), float(0.0201), float(0.00495), float(0.00495)]

def pickup_r(weight):
    picked_rarity = np.random.choice(rarities, p=weight)
    if picked_rarity == "SSR":
        picked_rarity = "SSRcard{}".format(random.randint(1, 91))
    if picked_rarity == "SR":
        picked_rarity = "SRcard{}".format(random.randint(1, 109))
    if picked_rarity == "R":
        picked_rarity = "Rcard{}".format(random.randint(1, 99))
    return picked_rarity

def pickup_r_2(weight2):
    picked_rarity_2 = np.random.choice(rarities2, p=weight2)
    if picked_rarity_2 == "SSR":
        picked_rarity_2 = "SSRcard{}".format(random.randint(1, 91))
    if picked_rarity_2 == "SR":
        picked_rarity_2 = "SRcard{}".format(random.randint(1, 109))
    return picked_rarity_2

def turn_r():
    result = []
    result.append(pickup_r(weight))
    return result

def turn_10r():
    result = []
    for i in range(9):
        result.append(pickup_r(weight))
    result.append(pickup_r_2(weight2))
    return result

gacha_result = []
gacha_result_list = []
jewel_used = 0
gacha_count = 0

for i in range(300):
    print("Gacha: 1 play or 10 plays")
    user_input = input()
    if user_input == 1:
        gacha_result.append(turn_r())
        gacha_result_list += gacha_result[i]
        jewel_used += 250
        gacha_count += 1
        if gacha_count == 300:
            print("You have reached maximum limit of plays allowed. Please take a card.")
            break
    print(gacha_result)    
    if user_input == 10: 
        gacha_result.append(turn_10r())
        gacha_result_list += gacha_result[i]
        jewel_used += 2500
        gacha_count += 10
        if gacha_count == 300:
            print("You have reached maximum limit of plays allowed. Please take a card.")
            break
    print(gacha_result)

r_counter = 0
sr_counter = 0
ssr_counter = 0
ssr_limited_counter = 0
ssr_new_counter = 0
sr_limited_counter = 0
sr_new_counter = 0

for element in gacha_result_list:
    if "R" in element:
        if ("SR" not in element) and ("SSR" not in element):
            r_counter += 1
    if ("SR" in element) and ("SSR" not in element):
        sr_counter += 1
    if "SSR" in element:
        ssr_counter += 1
    if "SRNew" in element:
        sr_new_counter += 1
    if "SRLimited" in element:
        sr_limited_counter += 1
    if "SSRLimited" in element:
        ssr_limited_counter += 1
    if "SSRNew" in element:
        ssr_new_counter += 1

def prob(counter):
    probability = float(counter / len(gacha_result_list)) * 100
    return probability