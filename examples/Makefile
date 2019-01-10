CXX = g++

all:
	$(CXX) -shared -fpic multiply.cpp -o libfoo.so
	$(CXX) main.cpp -L. -lfoo -o main
