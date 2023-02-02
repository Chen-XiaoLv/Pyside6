import matplotlib.pyplot as plt
import numpy as np
import math
x=[i for i in range(1,13)]
y=[12*(2*n**2-26*n+94) for n in x]
z=[abs(y[i]-y[i+1]) for i in range(11)]
print(y)
print(z)
# plt.plot(x,y)
# plt.show()