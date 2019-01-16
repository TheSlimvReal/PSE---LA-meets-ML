import h5py

##  Class that handles the saving of datasets
class Saver:

    ##  This method saves a dataset to a specified location
    #
    #   @param dataset that will be saved
    #   @param name under which it will be saved
    #   @param path where it will be saved
    @staticmethod
    def save(dataset, name: str, path: str) -> None:
        saving_file = h5py.File(path + name + '.hdf5', 'w')
        group = saving_file.create_group('dense_matrices')
        id_counter = 0
        for matrix in dataset:
            group.create_dataset('matrix_num_' + str(id_counter), data=matrix.todense())
            id_counter += 1



