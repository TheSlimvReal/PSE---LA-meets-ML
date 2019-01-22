from ctypes import *

class Ginkgowrapper:

        amount_of_iterations = 1

        def __init__(self, argc, argv):
                self.gingkowrapper = cdll.LoadLibrary("./ginkgowrapper.so")
                self.gingkowrapper.main(argc, create_string_buffer(str.encode("cuda"))
                self.gingkowrapper._Z41calculate_fastest_solver_on_square_matrixiPdPiiS0_S_S_i.restype = c_int


        def calculate_label(self, matrix_dense_Format):
                a_values = matrix_dense_Format.data
                a_ptrs = matrix_dense_Format.indptr
                a_row_indices = matrix_dense_Format.indices

                b = [1 for x in range(matrix_dense_Format.shape[0])]
                x = [0 for x in range(matrix_dense_Format.shape[0])]

                arrb = (c_double * len(b))(*b)
                arra = (c_double * len(a_values))(*a_values)
                arraptrs = (c_int * len(a_ptrs))(*a_ptrs)
                arrari = (c_int * len(a_row_indices))(*a_row_indices)
                arrx = (c_double * len(x))(*x)

                return self.gingkowrapper._Z41calculate_fastest_solver_on_square_matrixiPdPiiS0_S_S_i(matrix_dense_Format.shape[0], arra, arrari, len(a_values), arraptrs, arrb, arrx, self.amount_of_iterations)

