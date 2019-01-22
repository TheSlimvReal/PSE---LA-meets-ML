from modules.model.labeling_module.ginkgo import Ginkgowrapper
import h5py
import scipy.io
import scipy.sparse
import numpy as np

SolverOrder = ["cg", "bicgstab", "fcg", "cgs", "gmers"]

def main():
    cf = h5py.File("../../shared/data/example_matrices.hdf5")
    matrix_names = list(cf["dense_matrices"].keys())
    csr_matrices = []
    for name in matrix_names:
        csr_matrix = scipy.sparse.csr_matrix(np.array(cf["dense_matrices"][name]))
        csr_matrices.append(csr_matrix)

    g = Ginkgowrapper(2, "reference")

    matrices = []
    labels = []
    for matrix in csr_matrices:
        index = g.calculate_label(matrix)
        matrices.append(matrix.todense())
        label = np.array([0,0,0,0,0])
        label[index] = 1
        labels.append(label)
    new_dataset = [matrices, labels]
    print(new_dataset)

if __name__ == "__main__": main()