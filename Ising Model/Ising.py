import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
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
    for i in range(n-1):
        for j in range(n-1):
            Q = (J/(k*T)) * (x[i-1][j] + x[i+1][j] + x[i][j-1] + x[i][j+1])
            if Q <= 0:
                x[i][j] = 1
            else:
                x[i][j] = -1
    return x
# While loop.
i = 0
images = []
# Remove axes.
fig = plt.figure()
plt.axis('off')
# While loop.
while i < 50:
    images.append((plt.imshow(grid, cmap = 'Purples'),))
    grid = spin_change(grid, 1.602176565e-23, 1)
    i += 1
# Create animation.
ani = animation.ArtistAnimation(fig, images, interval = 700, repeat_delay = 1000, blit = True)

