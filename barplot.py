import numpy as np
import matplotlib.pyplot as plt
x = np.array(["White bread","Brown bread","Cakes"])
y = np.array([100,60,45])
plt.bar(x,y , color = 'brown')
plt.title("Sales in  Sanbake bakery",loc = 'left')
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()
