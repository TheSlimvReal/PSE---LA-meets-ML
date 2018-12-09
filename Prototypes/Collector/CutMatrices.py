import h5py
import numpy as np

f = h5py.File('C:/Users/Dennis/Documents/uni/PSE/Project/PSE---LA-meets-ML/Prototypes/Collector/494_bus.mat','r')

data = f.get('data/variable1')
data = np.array(data)
print(data)