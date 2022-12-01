import numpy as np
import matplotlib.pyplot as plt
import random
# Cost of a single pack.
cost = 0.80
# Function to open the pack and add new cards to the collection.
def pack_opener(cards_collected):
    pack = random.sample(range(1,830), 5)
    for i in range(len(pack)):
        cards_collected[i] += 1
    return cards_collected
# Simulate a single attempt to collect all the cards.
def single_sim_panini():
    amount = 0
    cards_collected = np.zeros(830) # List to keep track of cards collected.
    while(np.count_nonzero(cards_collected) != 830):
        collection = pack_opener(cards_collected)
        amount += cost
    return amount
