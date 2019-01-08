from modules.shared.matrix import Matrix


##This class handles the communication with the suit sparse matrix collection using the ssget tool
class SSGet:

    ##  Gets you a matrix
    #
    #   @return matrix that has been downloaded
    @staticmethod
    def get_matrix() -> Matrix:
        pass

    @staticmethod
    def __download_matrix() -> Matrix:
        pass

    @staticmethod
    def __cut_matrix(seed: int, matrix: Matrix) -> Matrix:
        pass
