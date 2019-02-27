from ctypes import *
import ctypes
import random


## This class is responsible for communicating with the c++ file(ginkgowrapper.cpp)
class Ginkgowrapper:

        __amount_of_iterations = 1
        __b_vector = []
        # The constructor for the class
        #
        # The b vector (from the linear system Ax=b,we are trying to solve)
        # gets set as a random vector in a specific shape
        # The shared library of the c++ file gets loaded with ctypes
        # The init function of the c++ gets called and the executors set
        # The result type of the c++ function calculate_time_with_solver_on_square_matrix gets set to an int
        #
        # @param self the instance of the class
        # @param argc a string which will determine the kind of executor which gets used in ginkgowrapper.cpp
        # @param argv a string which will determine the kind of executor which gets used in ginkgowrapper.cpp
        # @param shape the shape the b and s vector should have

        def __init__(self, argc, argv, shape):
                self.__b_vector = [random.uniform(0, 1) for x in range(shape)]
                self.gingkowrapper = ctypes.CDLL("modules/model/labeling_module/ginkgowrapper.so", mode=ctypes.RTLD_GLOBAL)
                self.gingkowrapper._Z8initExeciPc(argc, create_string_buffer(str.encode(argv)))
                self.gingkowrapper._Z43calculate_time_with_solver_on_square_matrixiPdPiiS0_S_S_ii.restype = ctypes.c_int

        # Calculate the time it takes to solve Ax=b with a specific solver by using the shared library
        #
        # This is achieved by converting the csr matrix format to vectors which we can give the function in the
        # shared library
        #
        # @param self the instance of the class
        # @param the matrix A in csr format
        # @param which solver should be used
        # @return the amount of time it to to solve Ax=b with the specified solver
        def calculate_time_to_solve(self, matrix_csr_format, which_solver):
                a_values = matrix_csr_format.data
                a_ptrs = matrix_csr_format.indptr
                a_row_indices = matrix_csr_format.indices

                x = [0 for x in range(matrix_csr_format.shape[0])]

                arrb = (c_double * len(self.__b_vector))(*self.__b_vector)
                arra = (c_double * len(a_values))(*a_values)
                arraptrs = (c_int * len(a_ptrs))(*a_ptrs)
                arrari = (c_int * len(a_row_indices))(*a_row_indices)
                arrx = (c_double * len(x))(*x)

                return self.gingkowrapper._Z43calculate_time_with_solver_on_square_matrixiPdPiiS0_S_S_ii(
                    matrix_csr_format.shape[0], arra, arrari, len(a_values), arraptrs,
                    arrb, arrx, self.__amount_of_iterations, which_solver)
