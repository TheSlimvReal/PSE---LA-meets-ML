#!/usr/bin/env python
import ctypes

libfoo = ctypes.cdll.LoadLibrary('./libfoo.so')

print(libfoo)
print(libfoo._Z8multiplyIiET_S0_S0_)

integer_multiply = libfoo._Z8multiplyIiET_S0_S0_
a = integer_multiply(3, 4)
print("Inside Python:", a)

