import numpy as np
import matplotlib.pyplot as plt
import random
# Cost of a single pack.
cost = 0.80
# Function to open the pack and add new cards to the collection.
def pack_opener(cards_collected):
    pack = random.sample(range(0,829), 5)
    for i in range(len(pack)):
        cards_collected[pack[i]] += 1
    return cards_collected
# Simulate a single attempt to collect all the cards.
def single_sim_panini(single_card_collection):
    number_of_packs = 0
    while(np.count_nonzero(single_card_collection) != 830):
        number_of_packs += 1
        single_card_collection = pack_opener(single_card_collection)
    return number_of_packs
# Simulate n sticker collection attempts.
def many_sim_panini(n):
    record_of_packs_opened = np.zeros(830)
    for i in range(n):
        collect_attempt = np.zeros(830)
        pack_attempt = single_sim_panini(collect_attempt)
        record_of_packs_opened[i] = pack_attempt
    return record_of_packs_opened
# Simulate n sticker collection attempts (cost).
def many_sim_panini_cost(record_of_packs_opened):
    n = len(record_of_packs_opened)
    record_of_cost = np.zeros(830)
    for i in range(n):
        record_of_cost[i] = record_of_packs_opened * cost
    return record_of_cost
# Statistical analysis of 10000 attempts.
pack_data = many_sim_panini(10000)
cost_data = many_sim_panini_cost(pack_data)
