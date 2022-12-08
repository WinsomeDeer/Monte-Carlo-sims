import numpy as np
import matplotlib.pyplot as plt
import random
# Initialise the grid.
n = 50
grid = np.ones((n,n), dtype = int) 
# Boltzman's constant.
k = 1.38 * 10 ** -27
# Create a random grid of 1's and -1's.
for i in range(n):
    for j in range(n):
        grid[i][j] = random.choice([-1,1])
# Function to iterate through the grid and calculate the new grid values.
def spin_change(x , J, T):
    for i in range(n):
        for j in range(n):
            Q = (J/(k*T)) * (grid[i-1][j] + grid[i+1][j] + grid[i][j-1] + grid[i][j+1])
