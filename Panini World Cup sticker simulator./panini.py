import numpy as np
import matplotlib.pyplot as plt
import random
# List to keep track of cards collected.
cards_collected = np.zeros(830)
cost = 0.80
# Function to open the pack.
def pack_opener():
    pack = random.sample(range(1,830), 5)
    return pack

    
    
    
