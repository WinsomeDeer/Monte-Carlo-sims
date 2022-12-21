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
        self.lattice = self.build_lattice()
    def build_lattice(self):
        return 2*np.random.randint(2, size=(self.n, self.n))-1
    # Lattice size method.
    @property
    def lattice_size(self):
        return {self.n, self.n}
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
                S = self.lattice[i,j]
                nn = (self.lattice[(i+1)%self.n, j] + self.lattice[(i-1)%self.n, j]
                         + self.lattice[i, (j+1)%self.n] + self.lattice[i, (j-1)%self.n])               
                Q = 2*S*nn
                if Q < 0:
                    S *= -1
                elif np.random.rand() < np.exp(-Q*1.0/self.T):
                    S *= -1
                self.lattice[i,j] = S
        return self.lattice
    # Function to run multiple iters and plot.
    def simulate(self):
        f = plt.figure(figsize = (15, 15), dpi = 80)
        self.plot(f, 0, 1)
        j = 2
        for i in range(1,101):
            self.one_itr(self.lattice)
            if np.abs(np.sum(self.lattice)) == self.n ** 2:
                self.plot(f, i, j)
                break
            if i == 1:
                self.plot(f, 1, j)
                j += 1
            if i == 10:
                self.plot(f, 10, j)
                j += 1
            if i == 50:
                self.plot(f, 50, j)
                j += 1
            if i == 75:
                self.plot(f, 75, j)
                j += 1
            if i == 100:
                self.plot(f, 100, j)
                j += 1
        plt.show()
    # Plotting function.
    def plot(self, f, i, N):
        X, Y = np.meshgrid(range(self.n+1), range(self.n+1))
        sp = f.add_subplot(3, 3, N)
        plt.setp(sp.get_xticklabels(), visible = False)   
        plt.setp(sp.get_yticklabels(), visible = False)    
        plt.pcolormesh(X, Y, self.lattice, cmap = plt.cm.RdBu)
        plt.title('Time=%d'%i)
        plt.axis('tight')
a = Ising_lattice(64, 0.1, 1.60218*10**(-19))
a.simulate()
