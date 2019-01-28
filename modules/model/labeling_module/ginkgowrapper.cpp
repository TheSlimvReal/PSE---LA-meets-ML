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
using vec = gko::matrix::Dense<>;
using val_array = gko::Array<double>;
using idx_array = gko::Array<int>;
using mtxDoubleInteger = gko::matrix::Csr<double, int>;
//typedef (*ScriptFunction)();


std::shared_ptr<gko::Executor> app_exec;
std::shared_ptr<gko::Executor> exec;
//std::map<std::string, int(*)()> Solvers;


int initExec(int argc, char *argv)
{
    // Figure out where to run the code
    if (argc == 1 || std::string(argv) == "reference") {
        exec = gko::ReferenceExecutor::create();
        printf("reference");
    } else if (argc == 2 && std::string(argv) == "omp") {
        exec = gko::OmpExecutor::create();
        printf("omp");
    } else if (argc == 2 && std::string(argv) == "cuda" &&
               gko::CudaExecutor::get_num_devices() > 0) {

        exec = gko::CudaExecutor::create(0, gko::OmpExecutor::create());
        printf("cuda");
    } else {
        printf("wrong");
        std::cerr << "Usage: " << argv[0] << " [executor]" << std::endl;
        std::exit(-1);
    }

	// figure it out!!
    app_exec = gko::ReferenceExecutor::create();

    //Solvers.emplace("Cg",gko::solver::Cg<>::build);
}

auto createDoubleVectorPointer(double values[],int amount_of_values) {

    vector<double> values_data (values,values + amount_of_values);
    double *values_data_p = values_data.data();
    return values_data_p;

}

int* createIntVectorPointer(int values[],int amount_of_values) {

    vector<int> values_data (values,values + amount_of_values);
    int * values_data_p = values_data.data();
    return values_data_p;

}

auto createIntPointer (vector<int> values_data) {

    int *values_data_p = values_data.data();

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
    vector<int> a_row_indices_data (a_row_indices,a_row_indices + a_amount_of_values);
    int *a_row_indices_p = a_row_indices_data.data();

    //create the Pointer to Vector of the Pointers to the rows
    vector<int>  a_ptrs_data (a_ptrs,a_ptrs + (dp + 1));
    int *a_ptrs_p = a_ptrs_data.data();


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


auto createSolver(std::shared_ptr<gko::matrix::Csr<double, int> >& A,int dp,auto (*pointer_to_Solver)()) {

    auto solver_gen =
        pointer_to_Solver()
            .with_criteria(
                gko::stop::Iteration::build().with_max_iters(dp).on(exec),
                gko::stop::ResidualNormReduction<>::build()
                    .with_reduction_factor(1e-20)
                    .on(exec))
            .on(exec);

    auto solver = solver_gen->generate(A);
    return solver;


}


int calculate_fastest_solver_on_square_matrix(int dp, double a_values[], int a_row_indices[], int a_amount_of_values, int a_ptrs[], double b_values[], double x_values[], int iterations_of_solvers,int whichSolver)
{

    gko::EnableDefaultFactory<gko::solver::Cg<>::Factory, gko::solver::Cg<>, gko::solver::Cg<>::parameters_type, gko::LinOpFactory>::parameters_type (*pointer_to_Solver2)() = gko::solver::Cg<>::build;
    /*
    char y = gko::solver::Cgs<>::build;
    char z = gko::solver::Gmres<>::build;
    char u = gko::solver::Fcg<>::build;
    char t = gko::solver:::Bicgstab::build;*/
    //create Ginkgo A Matrix
    auto A = share(createGinkgoMatrix(dp,a_values,a_row_indices,a_amount_of_values,a_ptrs));

    //create Ginkgo b Vector
    auto b = createGinkgoVector(dp,b_values);

    //create Ginkgo x Vector
    auto x = createGinkgoVector(dp,x_values);

    //vector<std::function<void()>> pointer_to_Solver2;
    switch ( whichSolver )
      {
         case 0:
            //cast pointer_to_solver to solver specific function and hope it works
            //(gko::EnableDefaultFactory<gko::solver::Cg<>::Factory, gko::solver::Cg<>, gko::solver::Cg<>::parameters_type, gko::LinOpFactory>::parameters_type (*)())
            //pointer_to_Solver2 =  gko::solver::Cg<>::build;
            break;
         case 1:
            //pointer_to_Solver = gko::solver::Bicgstab<>::build;
            break;
         case 2:
            //pointer_to_Solver = gko::solver::Fcg<>::build;
            break;
         case 3:
            //pointer_to_Solver = gko::solver::Cgs<>::build;
            break;
         case 4:
            //pointer_to_Solver = gko::solver::Gmres<>::build;
            break;
         default:
            exit(1);
      }

    auto solver = createSolver(A,dp,pointer_to_Solver2);
    /*
    auto solver_bicgstab = createSolver(A,dp,gko::solver::Bicgstab<>::build);

    
    auto solver_fcg = createSolver(A,dp,gko::solver::Fcg<>::build);
    
    auto solver_cgs = createSolver(A,dp,gko::solver::Cgs<>::build);
    
    auto solver_gmres = createSolver(A,dp,gko::solver::Gmres<>::build);*/


    // Solve system & save time
    high_resolution_clock::time_point t1,t2,t3,t4;
    double sum = 0;
    for(unsigned i = 0; i < iterations_of_solvers; i++){

        t1 = high_resolution_clock::now();
        solver->apply(lend(b), lend(x));
        t2 = high_resolution_clock::now();
        sum += (duration_cast<microseconds>( t2 - t1 ).count())/iterations_of_solvers;


    }
    return sum;
}

