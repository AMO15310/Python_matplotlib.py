import numpy as np
import matplotlib.pyplot as plt
x = np.array([600,450,300])
y = np.array(["White bread","Brown bread","Cakes"])
plt.pie(x,labels = y)
plt.title("Sales today at Sanbake bakery")
plt.show()

