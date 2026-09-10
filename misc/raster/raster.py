import numpy as np
from matplotlib import pyplot as plt

# use pyplot.imshow

# number of pixel grids
grids = 3
# number of sqrt(pixels) per grid
pixels = 2

dt = 'int' # fill in later with 3x3 matrices dtype
pixels = np.zeros(3, dtype=dt)

plt.imshow(pixels)