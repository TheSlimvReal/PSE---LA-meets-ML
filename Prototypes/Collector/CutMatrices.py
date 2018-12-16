import h5py
import numpy as np

f = h5py.File('494_bus.mat','r')

data = f.get('data/variable1')
data = np.array(data)
print(data)