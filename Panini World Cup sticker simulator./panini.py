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
def single_sim_panini(cards_collected):
    amount = 0
    while(np.count_nonzero(cards_collected) != 830):
        collection = pack_opener(cards_collected)
        amount += cost
    return amount
# Simulate n sticker collection attempts.
def many_sim_panini(n):
    record_of_cost = [0]*n
    for i in range(n):
        collect_attempt = []
        cost_attempt = single_sim_panini(collect_attempt)
        record_of_cost[i] = cost_attempt
    return record_of_cost
