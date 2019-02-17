# Numerical Linear Algebra meets Machine Learning

### Goal

This project tries to use a neural network to indicate which solver will be the fastest on a dense matrix.
It has been built for the practice of software engineering project at the KIT.

### Technology

For the neural network we used Keras.
To indicate the speed of the solver we used the Ginkgo library, which allows GPU-accelerated solvers.
The matrixes for testing/training are downloaded from the SuitSparse Matrix Collection with the SSGET command line tool by the Ginkgo group.