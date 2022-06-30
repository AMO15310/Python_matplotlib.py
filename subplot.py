import numpy as np
import matplotlib.pyplot as plt
#first plot
x = np.array([40,60,70,75,80])
y = np.array([50,70,80,90,100])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Sales")
plt.grid()
#second plot
a = np.array([50,70,75,80,85,90])
b = np.array([20,30,40,50,55,65])
plt.subplot(1,2,2)
plt.plot(a,b)
plt.title("Profits")
plt.grid()

plt.suptitle("My Shop")
plt.show()
