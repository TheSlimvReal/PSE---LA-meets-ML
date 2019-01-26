from modules.model.labeling_module.ginkgo import Ginkgowrapper
import h5py
import scipy.io
import scipy.sparse
import numpy as np
from modules.shared.saver import Saver

SolverOrder = ["cg", "bicgstab", "fcg", "cgs", "gmers"]


def main():

    cf = np.array(h5py.File("../../shared/data/labeled_matrices.hdf5")['dense_matrices'])
    csr_matrices = []
    for matrix in cf:
        csr_matrices.append(scipy.sparse.csr_matrix(np.real(matrix)))

    g = Ginkgowrapper(1, "reference")

    matrices = []
    labels = []
    for matrix in csr_matrices:
        index = g.calculate_label(matrix)
        matrices.append(matrix.todense())
        label = np.array([0, 0, 0, 0, 0])
        label[index] = 1
        labels.append(label)
    new_dataset = [matrices, labels]
    print(new_dataset)


if __name__ == "__main__":
    main()
