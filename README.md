# Linear Algebra meets Machine Learning - PSE Project

Linear Algebra meets Machine Learning is PSE Project from the Karlsruhe Institute of Technology. It uses a Convolutional Neural Network to find the fastest iterative solver for a given sparse linear system. It uses the C++ library ginkgo and the ssget tool.
## Motivation
Finding the solution of a sparse linear system is frequently occurring problem in physics, electrical engineering and other domains of science. When the linear systems get big enough it can take quite a while to solve them. This is why in big sparse linear systems iterative solvers are used to approximate a solution. There are different iterative solvers (our work includes Cgs, Cg, Fcg, Bicgstab and Fcg) which solve different linear systems at different speeds. We trained a neural network to identify which iterative solver solves a given linear system the fastest. You can now give our program a sparse matrix(from the linear system) in the hdf5 format and it will determine which solver will likely solve it the fastest.

## Installation

If you just want to classify a matrix you can simply clone our repo and start the program on your Linux or Windows device.
```bash
git clone https://github.com/TheSlimvReal/PSE---LA-meets-ML
```
If you however want to access our other functionality (including collecting, labeling and training, explained below) you will have to execute the program on a Linux device. Furthermore you will have to install a c++ compiler and cuda as well as the Ginkgo library (https://github.com/ginkgo-project/ginkgo) and ssget (https://github.com/ginkgo-project/ssget). The paths all of those programs have to be specified in our configuration file. 
## Usage
<<picture of the 4 modules here>>
Our main component is the classifier. Simply start our program by running run.py and insert 
```bash
classify path 
```
In the python shell. The path in this case is the full path to an hdf5 file, containing one matrix. The result will be for example:
```bash
The fastest iterative solver for your matrix is Cgs.
```
If you want to collect your own matrices from the suite sparse collection, type
```bash
collect amount size saving_path
```
Where amount is an integer which specifies how many matrices you want to collect, size is an integer specifying the size of the marices and saving_path a full path in which the matrices should be stored(may be an empty string, in which case a default value will be used)

As a result the matrices will be saved in one hdf5 file at the specified path.

If you want to label a set of matrices with their corresponding fastest iterative solver, you may use the command
```bash
label path saving_path name
```
Where path is a full path specifying which matrices to label(should be an hdf5 file), the saving_path specifies where to safe the matrices with its corresponding labels and the name is s string specifying how the saved hdf5 file should be named. All parameters may be an empty string in which case default values will be used.

If you want to train the neural network yourself you may type 
```bash
train path 
```
Where path is a full path specifying where the neural network which should be trained is.It may be an empty string in which case default values will be used.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Credit 

This Project was created by Anna Ricker, Simon Hanselmann, Yannick Funk, Fabian Koffer and Dennis Grötzinger

with the help and overseeing of the supervisors Hartwig Anzt and Markus Götz.



