import numpy as np
import h5py 
from scipy.io import loadmat
import matplotlib.pyplot as plt

f = loadmat('494_bus.mat') 
data = f['Problem']
data = np.array(data) # For converting to numpy array
sparse_values = data[0][0][1]
dense_values = sparse_values.todense()

plt.spy(dense_values)
plt.plot()