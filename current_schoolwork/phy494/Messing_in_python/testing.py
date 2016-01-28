import numpy as np
import matplotlib.pyplot as plt

y = []
x = []
n = 10
for i in range(1,n):
    y.append((np.cos((np.sqrt(i))))+i)
    #x.append(np.sin((0)))
plt.plot(y,'ro',label = ' cosine of consecutive integers ')
plt.plot(x,'b+',label = ' sine of consecutive integers ')
plt.show()






