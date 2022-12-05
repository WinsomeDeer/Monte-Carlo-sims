import numpy as np
import matplotlib.pyplot as plt
import random
# Simulate a single attempt to collect all the cards.
def single_sim_panini(single_card_collection):
    for i in range(10000):
        pack = random.sample(range(0,638), 5)
        for j in range(5):
            single_card_collection[pack[j]] = 0
        if np.sum(single_card_collection) == 0:
            break
    return i
# Simulate n sticker collection attempts.
def many_sim_panini(n):
    record_of_packs_opened = np.zeros((n,), dtype = int)
    for i in range(n):
        collect_attempt = np.ones((638,), dtype = int)
        pack_attempt = single_sim_panini(collect_attempt)
        record_of_packs_opened[i] = pack_attempt
    return record_of_packs_opened
# Simulate n sticker collection attempts (cost).
def many_sim_panini_cost(record_of_packs_opened):
    n = len(record_of_packs_opened)
    cost = 0.80
    record_of_cost = np.zeros((n,), dtype = int)
    for i in range(n):
        record_of_cost[i] = record_of_packs_opened[i] * cost
    return record_of_cost
# Statistical analysis of 10000 attempts.
pack_data = many_sim_panini(10000)
cost_data = many_sim_panini_cost(pack_data)
# Histograms of the data.
plt.hist(pack_data, bins = 100)
plt.hist(cost_data, bins = 100)
plt.show()
# Statistical quantities (packs).
mu_pack = np.mean(pack_data)
sigma_pack = np.std(pack_data)
LQ_pack = np.quantile(pack_data, 0.25)
median_pack = np.median(pack_data)
UQ_pack = np.quantile(pack_data, 0.75)
# Statistical quantities (cost).
mu_cost = np.mean(cost_data)
sigma_cost = np.std(cost_data)
LQ_cost = np.quantile(cost_data, 0.25)
median_cost = np.median(cost_data)
UQ_cost = np.quantile(cost_data, 0.75)
print(mu_pack)
print(mu_cost)
