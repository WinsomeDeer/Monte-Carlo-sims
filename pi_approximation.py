# Simple Monte Carlo simulation to approximate the value of pi.
import random
import numpy as np
import math
from turtle import *
import matplotlib.pyplot as plt
# Initialisation of variables.
inside_points = 0
r = 0.5
n = 5000
# For loop to calculate distance from centre of circle and count inside points.
for i in range(0,n):
    x = random.uniform(-r,r)
    y = random.uniform(-r,r)
    dist = math.sqrt(x**2 + y**2)
    if dist <= r :
        inside_points += 1
# Pi approximation based on ratio of points inside circle ans total points.
pi_approx = (inside_points)/n * 4
# Graphics to illustrate process.