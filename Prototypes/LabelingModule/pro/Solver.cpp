#include <ginkgo/ginkgo.hpp>

#include <fstream>
#include <iostream>
#include <string>
#include <time.h>
#include <chrono>

//shortcuts
using namespace std;
using namespace std::chrono;
std::shared_ptr<gko::Executor> app_exec;
std::shared_ptr<gko::Executor> exec;
auto createVector(double a_values[],int a_amount_of_values);
auto create_g_vektor(int shape, double b_values[]);

int main(int argc, char *argv)
{
    // Figure out where to run the code
    if (argc == 1 || std::string(argv) == "reference") {
        exec = gko::ReferenceExecutor::create();
    } else if (argc == 2 && std::string(argv) == "omp") {
        exec = gko::OmpExecutor::create();
    } else if (argc == 2 && std::string(argv) == "cuda" &&
               gko::CudaExecutor::get_num_devices() > 0) {
               std::cout << "he"<< "\n";
        exec = gko::CudaExecutor::create(0, gko::OmpExecutor::create());
    } else {
        std::cerr << "Usage: " << argv << " [executor]" << std::endl;
        std::exit(-1);
    }

        // figure it out!!
    app_exec = gko::OmpExecutor::create();
}

auto createVector(double a_values[],int a_amount_of_values) {
    vector<double> a_values_data (a_values,a_values + a_amount_of_values);
    return a_values_data;

}


auto create_g_vektor(int shape, double b_values[]) {
using cg = gko::solver::Cg<>;
    using vec = gko::matrix::Dense<>;
    using val_array = gko::Array<double>;
    using idx_array = gko::Array<int>;
    using mtxDoubleInteger = gko::matrix::Csr<double, int>;
    using bicgstab = gko::solver::Bicgstab<>;

    vector<double> b_values_Data (b_values, b_values + shape);
    double *b_values_p = b_values_Data.data();
    auto b = vec::create(exec, gko::dim<2>(shape, 1),val_array::view(app_exec, shape, b_values_p), 1);
    return b;
}

double calculate_time_with_SOLVERX_on_square_matrix(int shape, double a_values[], int a_row_indices[], int a_amount_of_values, int a_ptrs[], double b_values[], double x_values[])
{
    //shortcuts
    using cg = gko::solver::Cg<>;
    using vec = gko::matrix::Dense<>;
    using val_array = gko::Array<double>;
    using idx_array = gko::Array<int>;
    using mtxDoubleInteger = gko::matrix::Csr<double, int>;
    using bicgstab = gko::solver::Bicgstab<>;

    //create matrix A in ginkgo format
    //vector<double> a_values_data (a_values,a_values + a_amount_of_values);
    auto a_values_data = createVector( a_values, a_amount_of_values);
    double *a_values_data_p = a_values_data.data();
    vector<int> a_row_indices_data (a_row_indices,a_row_indices + a_amount_of_values);
    int *a_row_indices_p = a_row_indices_data.data();

    vector<int>  a_ptrs_data (a_ptrs,a_ptrs + (shape + 1));
    int *a_ptrs_p = a_ptrs_data.data();
    auto A = share(mtxDoubleInteger::create(exec, gko::dim<2>(shape),val_array::view(app_exec, a_amount_of_values, a_values_data_p),
                                        idx_array::view(app_exec, a_amount_of_values, a_row_indices_p),idx_array::view(app_exec, (shape + 1), a_ptrs_p)));

    //create b ginkgo vector
    vector<double> b_values_Data (b_values, b_values + shape);
    double *b_values_p = b_values_Data.data();
    //auto b = vec::create(exec, gko::dim<2>(shape, 1),val_array::view(app_exec, shape, b_values_p), 1);


    auto b = create_g_vektor(shape,b_values);
    //create x ginkgo vector
    vector<double> x_values_Data (x_values, x_values + shape);
    double *x_values_p = x_values_Data.data();
    auto x = vec::create(exec, gko::dim<2>(shape, 1),val_array::view(app_exec, shape, x_values_p), 1);

    // Generate solver Auslagern für mehr solver
    auto solver_gen =
        cg::build()
            .with_criteria(
                gko::stop::Iteration::build().with_max_iters(shape).on(exec),
                gko::stop::ResidualNormReduction<>::build()
                    .with_reduction_factor(1e-20)
                    .on(exec))
            .on(exec);
    //auto solver = solver_gen->generate(A);

    auto solver_bicg_gen =
        bicgstab::build()
            .with_criteria(
                gko::stop::Iteration::build().with_max_iters(shape).on(exec),
                gko::stop::ResidualNormReduction<>::build()
                    .with_reduction_factor(1e-20)
                    .on(exec))
            .on(exec);

    auto solver_bicg = solver_bicg_gen->generate(A);
    // Solve system & save time
        clock_t begin,end;
        double sum;
        for(unsigned i = 0; i < 10; i++){
                high_resolution_clock::time_point t1 = high_resolution_clock::now();
                auto solver = solver_gen->generate(A);
                solver->apply(lend(b), lend(x));
                high_resolution_clock::time_point t2 = high_resolution_clock::now();
                auto duration = duration_cast<microseconds>( t2 - t1 ).count();
                std::cout << ((double)(duration)) << "\n";
                sum = sum + duration;

        }
    return sum/10;
}
