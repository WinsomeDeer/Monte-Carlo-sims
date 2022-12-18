import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
# Class to initialise the grid.
k = 1.38 * 10 ** -27
# Lattice Class.
class Ising_lattice:
    # Constructor
    def __init__(self, n, temperature, J):
        self.n = n
        self.T = temperature
        self.lattice = self._build_lattice
        self.J = J
    # Lattice size method.
    @property
    def lattice_size(self):
        return {self.n, self.n}
    # Method to build the lattice.
    def _build_lattice(self, initial_state):
        if initial_state == 'r':
            lattice = np.random.choice([-1,1], self.n)
        elif initial_state == 'u':
            lattice = np.ones(self.n)
        else:
            raise ValueError(
                "Initial state must be either 'r' or 'u'."
            )
        return lattice
    # Method to calculate the energy at each point using nearest neighbour with periodic boundary conditions.
    def energy(self, i, j):
        Q = (-self.J/k*self.T)*(self.lattice[(i+1)%n][j] + self.lattice[(i-1)%n][j]
                         + self.lattice[i][(j+1)%n] + self.lattice[i][(j-1)%n])
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
                if self.energy(i, j) < 0:
                    lattice[i][j] = 1
                else:
                    lattice[i][j] = -1
    # Function to run multiple iters and plot.
    def simulate(self):
        lattice = self._build_lattice('u')
        fig = plt.figure(figsize = (15, 15), dpi = 80)
        self.plot(fig, lattice, 1, 1)
        for i in range(101):
            self.one_itr(lattice)
            if i == 1:
                self.plot(fig, lattice, 2, 2)
            if i == 25:
                self.plot(fig, lattice, 25, 3)
            if i == 50:
                self.plot(fig, lattice, 50, 4)
            if i == 75:
                self.plot(fig, lattice, 75, 5)
            if i == 100:
                self.plot(fig, lattice, 100, 6)
    # Plotting function.
    def plot(self, f, grid, i, N):
        X, Y = np.meshgrid(range(self.n), range(self.n))
        sp = f.add_subplot(3, 3, N)
        plt.setp(sp.get_xticklabels(), visible=False)      
        plt.pcolormesh(X, Y, grid, cmap=plt.cm.RdBu)
        plt.title('Time=%d'%i)
        plt.axis('tight')    
    plt.show()
