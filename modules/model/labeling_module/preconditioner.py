

##  Abstract class that represents the preconditioners which can be applied to a matrix to fasten the solving process
class Preconditioner:

    ##  Get the name of the preconditioner that will be understood by the ginkgo library
    #
    #   @return name of the preconditioner that can be used in ginkgo
    def get_preconditioner(self) -> str:
        pass
