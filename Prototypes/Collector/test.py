import os

#os.system('export CXX=/usr/local/bin/g++-6.4')
#os.system('export CC=/usr/local/bin/gcc-6.4')
#os.system('export PATH=$PATH:/usr/local/cuda-9.0/bin/')
#os.system('export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib')
#os.system('export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib')
#os.system('export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib64')
#os.system('$CXX test.cpp -shared -fpic -I/usr/local/include/ -L/usr/local/lib/-lginkgo_omp -lginkgo_reference -lginkgo -lginkgo_cuda -o testlibrary3.so')


os.environ['CXX'] = '/usr/local/bin/g++-6.4'
os.environ['CC'] = '/usr/local/bin/gcc-6.4'
os.environ['PATH'] = os.getenv("PATH","fail")+ ':/usr/local/cuda-9.0/bin/'
os.environ['LD_LIBRARY_PATH'] = '/usr/local/cuda/lib'
os.environ['LD_LIBRARY_PATH'] = os.getenv("LD_LIBRARY_PATH","fail")+':/usr/local/lib'
os.environ['LD_LIBRARY_PATH'] = os.getenv("LD_LIBRARY_PATH","fail")+':/usr/local/lib64'


#os will, in my understanding, generate a new sub shell in which the environment variables will be set
#thats why one can not just run p.py since it will be in another environment
os.system('python3.6 p.py')
#print(os.system('pwd'))
#print(os.environ)
#print(os.system('export'))
#print(os.system('python3.6 p.py'))

#ok