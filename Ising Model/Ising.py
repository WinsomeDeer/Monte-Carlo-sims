import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
# Class to initialise the grid.
n = 50
k = 1.38 * 10 ** -27
# Lattice Class.
class Ising_lattice:
    # Constructor
    def __init__(self, n, temperature, J):
        self.n = n
        self.T = temperature
        self.J = J
    # Lattice size method.
    @property
    def lattice_size(self):
        return {self.n, self.n}
    # Method to calculate the energy at each point using nearest neighbour with periodic boundary conditions.
    def energy(self, i, j, lattice):
        Q = 2*(lattice[i][j])*(lattice[(i+1)%n][j] + lattice[(i-1)%n][j]
                         + lattice[i][(j+1)%n] + lattice[i][(j-1)%n])
        return Q
    # Property of internal energy.
    @property
    def Internal_energy(self):
        e = 0 
        E = 0
        E_2 = 0
        # Calculate the energy for each cell.
        for i in range(self.n):
            for j in range(self.n):
                e = self.energy(i, j, self.J, self.T)
                E += e
                E_2 += e**2
        U = (1/self.n**2) * E
        U_2 = (1/self.n**2) * E_2
        return U, U_2
    # Heat capacity property.
    @property
    def heat_capacity(self):
        U, U_2 = self.Internal_energy
        return U_2 - U
    # Magnetisation property.
    @property
    def magnetisation(self):
        return np.abs(np.sum(self.lattice)/self.n**2)
    # Function to run one iteration.
    def one_itr(self, lattice):
        for i in range(self.n):
            for j in range(self.n):
                a  = np.random.randint(0, self.n)
                b  = np.random.randint(0, self.n)
                S = lattice[i][j]                
                Q = self.energy(a, b, lattice)
                if Q < 0:
                    S *= 1
                elif np.random.rand() < np.exp(-Q/self.T):
                    S *= -1
                lattice[i][j] = S
        return lattice
    # Function to run multiple iters and plot.
    def simulate(self):
        lattice = 2*np.random.randint(2, size=(self.n, self.n))-1
        f = plt.figure(figsize = (15, 15), dpi = 80)
        self.plot(f, lattice, 1, 1)
        for i in range(1001):
            self.one_itr(lattice)
            if i == 1:
                self.plot(f, lattice, 2, 2)
            if i == 250:
                self.plot(f, lattice, 250, 3)
            if i == 500:
                self.plot(f, lattice, 500, 4)
            if i == 750:
                self.plot(f, lattice, 750, 5)
            if i == 1000:
                self.plot(f, lattice, 1000, 6)
        plt.show()
    # Plotting function.
    def plot(self, f, grid, i, N):
        X, Y = np.meshgrid(range(self.n+1), range(self.n+1))
        sp = f.add_subplot(3, 3, N)
        plt.setp(sp.get_xticklabels(), visible=False)      
        plt.pcolormesh(X, Y, grid, cmap = plt.cm.RdBu)
        plt.title('Time=%d'%i)
        plt.axis('tight')
a = Ising_lattice(50, 0.1, 1.60218*10**(-19))
a.simulate()
