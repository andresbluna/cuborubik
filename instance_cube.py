import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np

axes = [5, 5, 5]

data = np.ones(axes)

alpha = 0.9

colors = np.empty(axes + [4])
colors[0] = [1, 0, 0, alpha]
colors[1] = [0, 1, 0, alpha]
colors[2] = [0, 0, 1, alpha] 
colors[3] = [1, 1, 0, alpha]
colors[4] = [1, 1, 1, alpha] 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.axis('off')

ax.voxels(data, facecolors=colors, edgecolors='grey')

plt.show()
