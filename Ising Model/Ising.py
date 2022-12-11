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
    def __init__(self, n, temperature):
        self.n = n
        self.T = temperature
        self.lattice = self._build_lattice
    
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
    # Method to calculate the energy at each point using nearest neighbour.
    def energy(self, i, j, J, T):
        Q = (-J/k*T)*(self.lattice[i+1][j] + self.lattice[i-1][j]
                         + self.lattice[i][j+1] + self.lattice[i][j-1])
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
# Function to run the program.

