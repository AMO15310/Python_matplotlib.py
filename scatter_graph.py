import numpy as np
from numpy import random
import matplotlib.pyplot as plt
x = np.random.randint(100, size = (10))
y = np.random.randint(100,size=(10))
plt.scatter(x,y, color = 'hotpink')
plt.title("A random scatter graph")
plt.show()
