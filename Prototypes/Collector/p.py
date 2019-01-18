#import ctypes
import os
from ctypes import *
#charptr = POINTER(c_char)
#os.system('scp -r ugsqo@lsdf-28-131.scc.kit.edu:/tmp/pycharm_project_213/Prototypes/Collector/testlibrary.so C:/Users/Dennis/Documents/uni/PSE/Project/PSE---LA-meets-ML/Prototypes/Collector')
mutable_string = create_string_buffer(str.encode("real"))
#mystr1=c_char_p("mystring")
a = 1

test = CDLL('/home/ugsqo/home/ugsqo/Prototypes/Collector/testlibrary4.so')
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