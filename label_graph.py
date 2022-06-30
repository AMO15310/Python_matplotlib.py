import numpy as np
import matplotlib.pyplot as plt
x = np.array([10,15,20,25,30,35])
y = np.array([200,250,300,350,400,450])
plt.plot(x,y)
plt.title("Production against sales in a bakery", loc = 'left')
plt.xlabel("No of flour bags")
plt.ylabel("Sales rate in a certain route")
plt.show()
