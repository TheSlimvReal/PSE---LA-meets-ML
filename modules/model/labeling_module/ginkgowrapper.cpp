#include <ginkgo/ginkgo.hpp>

#include <fstream>
#include <iostream>
#include <string>
#include <time.h>
#include <chrono>
#include <stdio.h>
#include <stdlib.h>

//shortcuts
using namespace std;
using namespace std::chrono;
using vec = gko::matrix::Dense<>;
using val_array = gko::Array<double>;
using idx_array = gko::Array<int>;
using mtxDoubleInteger = gko::matrix::Csr<double, int>;
std::shared_ptr<gko::Executor> app_exec;
std::shared_ptr<gko::Executor> exec;
auto createDoubleVectorPointer(double a_values[],int a_amount_of_values);
int* createIntVectorPointer(double a_values[],int a_amount_of_values);
auto createGinkgoMatrix(int dp, int a_amount_of_values, int a_values[]);
auto createIntVector(int values[],int amount_of_values);
auto createIntPointer (vector<int> values_data);
auto createGinkgoVector(int dp, double values[]);
int main(int argc, char *argv)
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

	// figure it out!!
    app_exec = gko::OmpExecutor::create();
}

auto createDoubleVectorPointer(double values[],int amount_of_values) {
    vector<double> values_data (values,values + amount_of_values);
    double *values_data_p = values_data.data();
    return values_data_p;

}

int* createIntVectorPointer(int values[],int amount_of_values) {
    vector<int> values_data (values,values + amount_of_values);
    /*
    int *values_data_p;
    values_data_p = (int*) malloc(sizeof(int));
    if (values_data_p==NULL) {printf("error");}
    printf("%d", *values_data.data());
    *values_data_p = *values_data.data();
    printf("%d", *values_data_p);

    //vector<int> a_row_indices_data (a_row_indices,a_row_indices + a_amount_of_values);
    int *a_row_indices_p = a_row_indices_data.data();

    return values_data_p;*/
    int * values_data_p = values_data.data();
    return values_data_p;

}

auto createIntPointer (vector<int> values_data) {

    int *values_data_p = values_data.data();

    //vector<int> a_row_indices_data (a_row_indices,a_row_indices + a_amount_of_values);
    //int *a_row_indices_p = a_row_indices_data.data();

    return values_data_p;
}

auto createIntVector(int values[],int amount_of_values) {
    vector<int> values_data (values,values + amount_of_values);

    return values_data;

}


auto createGinkgoMatrix(int dp, double a_values[], int a_row_indices[], int a_amount_of_values, int a_ptrs[]) {

    //create the Pointer to Vector of the Values of A
    auto a_values_data_p = createDoubleVectorPointer(a_values,a_amount_of_values);
    //create the Pointer to Vector of the Row Indices
    //auto a_row_indices_p = createIntVectorPointer(a_row_indices,a_amount_of_values);
    //create the Pointer to Vector of the Pointers to the rows
    vector<int> a_row_indices_data (a_row_indices,a_row_indices + a_amount_of_values);
    int *a_row_indices_p = a_row_indices_data.data();

    //int *a_row_indices_p = (int*)malloc(sizeof(int));
    //a_row_indices_p = createIntPointer(a_row_indices_data);

    vector<int>  a_ptrs_data (a_ptrs,a_ptrs + (dp + 1));

    int *a_ptrs_p = a_ptrs_data.data();
    //auto a_ptrs_p = createIntVectorPointer(a_ptrs,dp+1);

    auto A = mtxDoubleInteger::create(exec, gko::dim<2>(dp),
                                val_array::view(app_exec, a_amount_of_values, a_values_data_p),
                                idx_array::view(app_exec, a_amount_of_values, a_row_indices_p),
                                idx_array::view(app_exec, (dp + 1), a_ptrs_p));

    return A;

}

auto createGinkgoVector(int dp, double values[]) {

    auto values_data_p = createDoubleVectorPointer(values,dp);
    auto b = vec::create(exec, gko::dim<2>(dp, 1),val_array::view(app_exec, dp, values_data_p), 1);
    return b;
}

int calculate_fastest_solver_on_square_matrix(int dp, double a_values[], int a_row_indices[], int a_amount_of_values, int a_ptrs[], double b_values[], double x_values[], int iterations_of_solvers)
{

    //create Ginkgo A Matrix
    auto A = share(createGinkgoMatrix(dp,a_values,a_row_indices,a_amount_of_values,a_ptrs));

    //create Ginkgo b Vector
    auto b = createGinkgoVector(dp,b_values);

    //create Ginkgo x Vector
    auto x = createGinkgoVector(dp,x_values);

    // Generate solver Auslagern für mehr solver
    auto solver_gen_cg =
        gko::solver::Cg<>::build()
            .with_criteria(
                gko::stop::Iteration::build().with_max_iters(dp).on(exec),
                gko::stop::ResidualNormReduction<>::build()
                    .with_reduction_factor(1e-20)
                    .on(exec))
            .on(exec);
    auto solver_cg = solver_gen_cg->generate(A);

    auto solver_gen_bicgstab =
        gko::solver::Bicgstab<>::build()
            .with_criteria(
                gko::stop::Iteration::build().with_max_iters(dp).on(exec),
                gko::stop::ResidualNormReduction<>::build()
                    .with_reduction_factor(1e-20)
                    .on(exec))
            .on(exec);

    auto solver_bicgstab = solver_gen_bicgstab->generate(A);

    auto solver_gen_fcg =
        gko::solver::Fcg<>::build()
            .with_criteria(
                gko::stop::Iteration::build().with_max_iters(dp).on(exec),
                gko::stop::ResidualNormReduction<>::build()
                    .with_reduction_factor(1e-20)
                    .on(exec))
            .on(exec);

    auto solver_fcg = solver_gen_fcg->generate(A);

    auto solver_gen_cgs =
        gko::solver::Cgs<>::build()
            .with_criteria(
                gko::stop::Iteration::build().with_max_iters(dp).on(exec),
                gko::stop::ResidualNormReduction<>::build()
                    .with_reduction_factor(1e-20)
                    .on(exec))
            .on(exec);

    auto solver_cgs = solver_gen_cgs->generate(A);

    auto solver_gen_gmres =
        gko::solver::Gmres<>::build()
            .with_criteria(
                gko::stop::Iteration::build().with_max_iters(dp).on(exec),
                gko::stop::ResidualNormReduction<>::build()
                    .with_reduction_factor(1e-20)
                    .on(exec))
            .on(exec);

    auto solver_gmres = solver_gen_gmres->generate(A);

    // Solve system & save time
    high_resolution_clock::time_point t1,t2,t3,t4;
    double sums[] = {0,0,0,0,0};
    for(unsigned i = 0; i < iterations_of_solvers; i++){

        t1 = high_resolution_clock::now();
        solver_cg->apply(lend(b), lend(x));
        t2 = high_resolution_clock::now();
        sums[0] += (duration_cast<microseconds>( t2 - t1 ).count())/iterations_of_solvers;

        t1 = high_resolution_clock::now();
        solver_bicgstab->apply(lend(b), lend(x));
        t2 = high_resolution_clock::now();
        sums[1] += (duration_cast<microseconds>( t2 - t1 ).count())/iterations_of_solvers;

        t1 = high_resolution_clock::now();
        solver_fcg->apply(lend(b), lend(x));
        t2 = high_resolution_clock::now();
        sums[2] += (duration_cast<microseconds>( t2 - t1 ).count())/iterations_of_solvers;

        t1 = high_resolution_clock::now();
        solver_cgs->apply(lend(b), lend(x));
        t2 = high_resolution_clock::now();
        sums[3] += (duration_cast<microseconds>( t2 - t1 ).count())/iterations_of_solvers;

        t1 = high_resolution_clock::now();
        solver_gmres->apply(lend(b), lend(x));
        t2 = high_resolution_clock::now();
        sums[4] += (duration_cast<microseconds>( t2 - t1 ).count())/iterations_of_solvers;
    }
    double min = sums[0];
    int fastestCalcNumber = 0;
    for(unsigned i = 1; i < 5; i++){
        //std::cout << sums[i] <<"\n";
        if(min > sums[i]){
            min = sums[i];
            fastestCalcNumber = i;
        }
    }
    return fastestCalcNumber;
}

