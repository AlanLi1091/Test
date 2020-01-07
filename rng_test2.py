import numpy as np
import random

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

gacha_result_10 = []
gacha_result_10_list = []
for i in range(10):
    gacha_result_10.append(turn_10r())
    gacha_result_10_list += gacha_result_10[i]

r_num = gacha_result_10_list.count('Rcard{}'.format(random.randint(1, 99)))
print(r_num)
sr_num = gacha_result_10_list.count('SR')
ssr_num = gacha_result_10_list.count('SSR')