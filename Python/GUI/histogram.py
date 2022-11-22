import matplotlib.pyplot as plt
import numpy as np

arr=[12,23,45,56,78,73,48,94,63,59,33,37]

fig, ax = plt.subplots(figsize=(10,10))
ax.hist(arr, bins=[0,25,50,75,100],range=(0,100) ,histtype = 'bar')

plt.show()