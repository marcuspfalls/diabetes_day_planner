import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import math

def sigmoid(x,u,t):
    z = np.exp(-x*3)
    sig = 1.5*u*(1 / (1 + z))
    return sig

a = np.linspace(-6,6,100)
b = sigmoid(a,3,4)
plt.plot(a,b)

plt.show()
plt.savefig('test.png')



