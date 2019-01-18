#import ctypes
import os
from ctypes import *
#charptr = POINTER(c_char)
#os.system('scp -r ugsqo@lsdf-28-131.scc.kit.edu:/tmp/pycharm_project_213/Prototypes/Collector/testlibrary.so C:/Users/Dennis/Documents/uni/PSE/Project/PSE---LA-meets-ML/Prototypes/Collector')
#import os
#os.environ['CXX'] = '/usr/local/bin/g++-6.4'
#os.environ['CC'] = '/usr/local/bin/gcc-6.4'
#os.environ['PATH'] = os.getenv("PATH","fail")+ ':/usr/local/cuda-9.0/bin/'
#os.environ['LD_LIBRARY_PATH'] = '/usr/local/cuda/lib'
#os.environ['LD_LIBRARY_PATH'] = os.getenv("LD_LIBRARY_PATH","fail")+':/usr/local/lib'
#os.environ['LD_LIBRARY_PATH'] = os.getenv("LD_LIBRARY_PATH","fail")+':/usr/local/lib64'

#os.system('$CXX test.cpp -shared -fpic -I/usr/local/include/ -L/usr/local/lib/-lginkgo_omp -lginkgo_reference -lginkgo -lginkgo_cuda -o testlibrary3.so')

mutable_string = create_string_buffer(str.encode("real"))





#mystr1=c_char_p("mystring")
a = 1

test = CDLL('/home/ugsqo/home/ugsqo/Prototypes/Collector/testlibrary3.so')
#test.blub.argtypes = []
#test.initializetest.restype = charptr
#test._Z4blubNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE.argtypes = [charptr]
#test._Z4blubNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE.restype = c_int



function = test._Z4blubPc
#function.argtypes[ctypes.POINTER(ctypes.c_char)]


#test._Z10testStringv()
print(mutable_string.value)
function(mutable_string)
print(mutable_string.value)