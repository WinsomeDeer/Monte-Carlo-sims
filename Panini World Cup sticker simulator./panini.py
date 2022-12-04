import numpy as np
import matplotlib.pyplot as plt
import random
# Cost of a single pack.
cost = 0.80
# Function to open the pack and add new cards to the collection.
def pack_opener(cards_collected):
    pack = random.sample(range(1,830), 5)
    for i in range(len(pack)):
        cards_collected[pack[i]] += 1
    return cards_collected
# Simulate a single attempt to collect all the cards.
def single_sim_panini():
    number_of_packs = 0
    collect = []
    cards_collected = np.zeros(830) # List to keep track of cards collected.
    while(np.count_nonzero(cards_collected) != 830):
        number_of_packs += 1
        collect = pack_opener(cards_collected)
    return number_of_packs
# Simulate n sticker collection attempts.
def many_sim_panini(n):
    record_of_packs_opened = [0]*n
    for i in range(n):
        collect_attempt = []
        pack_attempt = single_sim_panini(collect_attempt)
        record_of_packs_opened[i] = pack_attempt
    return record_of_packs_opened
# Simulate n sticker collection attempts (cost).
def many_sim_panini_cost(record_of_packs_opened):
    n = len(record_of_packs_opened)
    record_of_cost = [0]*n
    for i in range(n):
        record_of_cost[i] = record_of_packs_opened * cost
    return record_of_cost
# Statistical analysis of 10000 attempts.
pack_data = many_sim_panini(10000)
cost_data = many_sim_panini_cost(pack_data)
