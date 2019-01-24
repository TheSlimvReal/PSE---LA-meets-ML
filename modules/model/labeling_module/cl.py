import os

os.environ['CXX'] = '/usr/local/bin/g++-6.4'
os.environ['CC'] = '/usr/local/bin/gcc-6.4'
os.environ['PATH'] = os.getenv("PATH", "fail") + ':/usr/local/cuda-9.0/bin/'
os.environ['LD_LIBRARY_PATH'] = '/usr/local/cuda/lib'
os.environ['LD_LIBRARY_PATH'] = os.getenv("LD_LIBRARY_PATH", "fail") + ':/usr/local/lib'
os.environ['LD_LIBRARY_PATH'] = os.getenv("LD_LIBRARY_PATH", "fail") + ':/usr/local/lib64'

os.system("$CXX  ginkgowrapper.cpp -shared -fpic -I/usr/local/include/ -L/usr/local/lib/ "
          "-lginkgo_omp -lginkgo_reference -lginkgo -lginkgo_cuda -o ginkgowrapper.so")
os.system('python3.6 testLabel.py')
