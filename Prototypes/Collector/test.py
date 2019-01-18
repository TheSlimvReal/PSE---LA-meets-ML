import os

os.system('export CXX=/usr/local/bin/g++-6.4')
os.system('export CC=/usr/local/bin/gcc-6.4')
os.system('export PATH=$PATH:/usr/local/cuda-9.0/bin/')
os.system('export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib')
os.system('export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib')
os.system('export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib64')
#os.system('$CXX test.cpp -shared -fpic -I/usr/local/include/ -L/usr/local/lib/-lginkgo_omp -lginkgo_reference -lginkgo -lginkgo_cuda -o testlibrary3.so')



print(os.system('pwd'))
#print(os.environ)
#print(os.system('export'))
#print(os.system('python3.6 p.py'))

#ok