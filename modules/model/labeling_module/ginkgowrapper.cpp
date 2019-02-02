/*
This class is used to communicate with ginkgo. It calculates the time a iterative solver needs to solve a matrix.
The class will be compiled as a shared library which we will load from python with ctypes.

*/

#include </usr/local/include/ginkgo/ginkgo.hpp>
#include <fstream>
#include <iostream>
#include <string>
#include <time.h>
#include <chrono>
#include <stdio.h>
#include <stdlib.h>
#include <map>

//shortcuts
using namespace std;
using namespace std::chrono;
std::unique_ptr<gko::LinOp> gen(std::shared_ptr<gko::matrix::Csr<double, int> >& A, int dp);
typedef std::unique_ptr<gko::LinOp> (*solver_function) (std::shared_ptr<gko::matrix::Csr<double, int> >& A, int dp);
using vec = gko::matrix::Dense<>;
using val_array = gko::Array<double>;
using idx_array = gko::Array<int>;
using mtxDoubleInteger = gko::matrix::Csr<double, int>;

std::shared_ptr<gko::Executor> app_exec;
std::shared_ptr<gko::Executor> exec;
std::map<int, solver_function> m;

/*
Initialize the executor on which the execution will take place and the executor which specifies where the data is.
@params argc either 1 or 2
@params *argv the string which specifies the executor; either reference, omp or cuda
*/
int initExec(int argc, char *argv)
{
    // Figure out where to run the code
    if (argc == 1 || std::string(argv) == "reference") {
        exec = gko::ReferenceExecutor::create();
    } else if (argc == 2 && std::string(argv) == "omp") {
        exec = gko::OmpExecutor::create();
    } else if (argc == 2 && std::string(argv) == "cuda" &&
               gko::CudaExecutor::get_num_devices() > 0) {


        exec = gko::CudaExecutor::create(0, gko::OmpExecutor::create());
    } else {

        std::cerr << "Usage: " << argv[0] << " [executor]" << std::endl;
        std::exit(-1);
    }

    app_exec = gko::ReferenceExecutor::create();




}
/*
create a Pointer to a vector which has doubles as values
@params values the values
@params amount_of_values the amount of values
*/
auto createDoubleVectorPointer(double values[],int amount_of_values) {
    vector<double> values_data (values,values + amount_of_values);
    double *values_data_p = values_data.data();
    return values_data_p;
}
/*
create a Pointer to a vector which has ints as values
!DOES NOT WORK!
@params values the values
@params amount_of_values the amount of values
*/
auto createIntVectorPointer(int values[],int amount_of_values) {
    vector<int> values_data (values,values + amount_of_values);
    int * values_data_p = values_data.data();
    return values_data_p;
}


/*
create a ginkgo matrix from a matrix in the csr format(split as individual arrays)
@params dp the discretization points
@params a_values the values of the matrix
@params a_row_indizies the row inidizies of the matrix
@params a_amount_of_values the amount of values in the matrix
@params a_ptrs the pointers to the rows of the matrix
*/
auto createGinkgoMatrix(int dp, double a_values[], int a_row_indices[], int a_amount_of_values, int a_ptrs[]) {

    //create the Pointer to Vector of the Values of A

    auto a_values_data_p = createDoubleVectorPointer(a_values,a_amount_of_values);

    //create the Pointer to Vector of the Row Indices
    vector<int> a_row_indices_data (a_row_indices,a_row_indices + a_amount_of_values);
    int *a_row_indices_p = a_row_indices_data.data();
    //int* a_row_indices_p = createIntVectorPointer(a_row_indices,a_amount_of_values);
    //create the Pointer to Vector of the Pointers to the rows
    vector<int>  a_ptrs_data (a_ptrs,a_ptrs + (dp + 1));

    int *a_ptrs_p = a_ptrs_data.data();
    //int *a_ptrs_p = createIntVectorPointer(a_ptrs,dp+1);

    auto A = mtxDoubleInteger::create(exec, gko::dim<2>(dp),
                                val_array::view(app_exec, a_amount_of_values, a_values_data_p),
                                idx_array::view(app_exec, a_amount_of_values, a_row_indices_p),
                                idx_array::view(app_exec, (dp + 1), a_ptrs_p));
    return A;

}
/*
create a Ginkgo vector with discretization points and certain values
@params dp the discretization points
@params values the values of the vector
*/
auto createGinkgoVector(int dp, double values[]) {
    auto values_data_p = createDoubleVectorPointer(values,dp);
    auto b = vec::create(exec, gko::dim<2>(dp, 1),val_array::view(app_exec, dp, values_data_p), 1);
    return b;
}
/*
create a solver by applaying a certain solver factory to a ginkgo matrix
@params A the ginkgo matrix
@params dp the discretization points
@params pointer_to_Solver a pointer to a certain kind of solver(Cg,Bicgstab,Cgs,Fcg or Gmres)
*/
auto createSolver(std::shared_ptr<gko::matrix::Csr<double, int> >& A,int dp,auto (*pointer_to_Solver)()) {

    auto solver_gen =
        pointer_to_Solver()
            .with_criteria(
                gko::stop::Iteration::build().with_max_iters(dp).on(exec),
                gko::stop::ResidualNormReduction<>::build()
                    .with_reduction_factor(1e-6)
                    .on(exec))
            .on(exec);

    auto solver = solver_gen->generate(A);
    return solver;

}


template <typename T>
std::unique_ptr<gko::LinOp> gen(std::shared_ptr<gko::matrix::Csr<double, int> >& A, int dp) {
    return T::build()
	.with_criteria(
		gko::stop::Iteration::build().with_max_iters(dp).on(exec),
                gko::stop::ResidualNormReduction<>::build()
			.with_reduction_factor(1e-20)
			.on(exec))
        .on(exec)->generate(A);
}
typedef std::unique_ptr<gko::LinOp> (*solver_function) (std::shared_ptr<gko::matrix::Csr<double, int> >& A, int dp);

/*
calculates the time a certain solver takes to solve the system Ax=b, given by the inputs (A given in csr format)
@params dp the discretization points
@params a_values the values of the matrix
@params a_row_inicies the row indicies of the matrix
@params a_amount_of_values the amount of values in the matrix
@params a_ptrs pointers to the rows of the matrix
@params b_values the values of the b vector
@params x_values the values of the x vector
@params iterations_of_solvers how often each solver should be applied
@params whichSolver which solver should be used Cg,Bicgstab,Cgs,Fcg or Gmres, coded as ints as it is specified in the python code)


*/

int calculate_time_with_solver_on_square_matrix(int dp, double a_values[], int a_row_indices[], int a_amount_of_values,
    int a_ptrs[], double b_values[], double x_values[], int iterations_of_solvers, int whichSolver)
{

    m[0] = gen<gko::solver::Bicgstab<> >;
    m[1] = gen<gko::solver::Cg<> >;
    m[2] = gen<gko::solver::Cgs<> >;
    m[3] = gen<gko::solver::Fcg<> >;
    //m[4] = gen<gko::solver::Gmres<> >;


    //gko::LinOp* solver44 = gko::solver::Bicgstab<>;
    //map<string,int(*)()> int_map;
    //create Ginkgo A Matrix
    auto A = share(createGinkgoMatrix(dp,a_values,a_row_indices,a_amount_of_values,a_ptrs));

    //create Ginkgo b Vector
    auto b = createGinkgoVector(dp,b_values);

    //create Ginkgo x Vector
    auto x = createGinkgoVector(dp,x_values);

    high_resolution_clock::time_point t1,t2;
    double sum = 0;

    auto solver = m[whichSolver](A,dp);
          sum = 0;
          for(unsigned i = 0; i < iterations_of_solvers; i++){

                t1 = high_resolution_clock::now();
                solver->apply(lend(b), lend(x));
                t2 = high_resolution_clock::now();
                sum += (duration_cast<microseconds>( t2 - t1 ).count())/iterations_of_solvers;
          }

    return sum;

}

