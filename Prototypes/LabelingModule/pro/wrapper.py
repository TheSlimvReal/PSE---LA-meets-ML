import ctypes
import h5py
import scipy.io
import scipy.sparse
import numpy as np

def main():
        s = ctypes.cdll.LoadLibrary("/home/ugsqo/home/ugsqo/Prototypes/LabelingModule/pro/lib.so")
        cf = h5py.File("data/example_matrices.hdf5")
        matrix_names = list(cf["dense_matrices"].keys())
        csr_matrices = []
        for name in matrix_names:
                csr_matrix = scipy.sparse.csr_matrix(np.array(cf["dense_matrices"][name]))
                csr_matrices.append(csr_matrix)

        a_values = csr_matrices[0].data
        a_ptrs = csr_matrices[0].indptr
        a_row_indices = csr_matrices[0].indices

        b = [1 for x in range(csr_matrices[0].shape[0])]
        x = [0 for x in range(csr_matrices[0].shape[0])]

        arrb = (ctypes.c_double * len(b))(*b)
        arra = (ctypes.c_double * len(a_values))(*a_values)
        arraptrs = (ctypes.c_int * len(a_ptrs))(*a_ptrs)
        arrari = (ctypes.c_int * len(a_row_indices))(*a_row_indices)
        arrx = (ctypes.c_double * len(x))(*x)

        s.main(1, "omp")
        s._Z44calculate_time_with_SOLVERX_on_square_matrixiPdPiiS0_S_S_.restype = ctypes.c_double
        t = s._Z44calculate_time_with_SOLVERX_on_square_matrixiPdPiiS0_S_S_(csr_matrices[0].shape[0], arra, arrari, len(a_values), arraptrs, arrb, arrx)
        print("durchschnittliche zeit von 10 runs:", t)

if __name__=="__main__":main()






