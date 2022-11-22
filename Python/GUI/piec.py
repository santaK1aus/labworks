import matplotlib.pyplot as plt
import numpy as np

y = [12,28,20,25,5]
labels=['Maths','English','Geography','Science','History']
expl = [0.1,0,0,0,0]
plt.pie(y,labels=labels,explode=expl,shadow=True)

plt.show()