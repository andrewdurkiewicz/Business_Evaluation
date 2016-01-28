import numpy as np
import matplotlib.pyplot as plt
n = 10
x = []
i = 0
while i <= n:
    cos = np.cos(i * np.pi)
    x.append(cos)
    i+=0.001
plt.plot(x)
plt.show()
