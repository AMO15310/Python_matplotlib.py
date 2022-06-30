import numpy as np
import matplotlib.pyplot as plt
x = np.array([4,5,6,7,8])
y = np.array([40,35,30,25,20])
plt.plot(x,y)
plt.title("Resistance against current graph",loc = 'left')
plt.xlabel("Resistance in ohms")
plt.ylabel("Current in Amps")
plt.grid()
plt.show()
