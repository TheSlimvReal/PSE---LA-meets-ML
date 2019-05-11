#!/usr/bin/env bash

mkdir $HOME/bin
ln -s /usr/local/bin/gcc-6.4 $HOME/bin/gcc
ln -s /usr/local/bin/g++-6.4 $HOME/bin/g++

unset PATH
unset CXX
unset CC
unset LD_LIBRARY_PATH

export PATH=$HOME/bin:$PATH
export CXX=/usr/local/bin/g++-6.4
export CC=/usr/local/bin/gcc-6.4
export PATH=$PATH:/usr/local/bin/:/usr/local/cuda/bin/:/usr/bin/:/bin:/usr/sbin/:/sbin
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda/lib64/
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib64

cd $HOME
git clone https://github.com/ginkgo-project/ginkgo.git
cd ginkgo
mkdir build
cd build
cmake -DGINKGO_BUILD_CUDA=ON -DGINKGO_BUILD_OMP=ON ..
make -j30
cd benchmark
make benchmark SYSTEM_NAME=K80 BENCHMARK=solver DRY_RUN=flase EXECUTOR=cuda SEGMENTS=1000 SEGMENT_ID=1
cd $HOME