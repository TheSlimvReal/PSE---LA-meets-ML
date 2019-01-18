#include <ginkgo/ginkgo.hpp>
#include <fstream>
#include <iostream>
#include <string>

int main(int argc, char *argv[])
{// Print  version information
	std::cout << gko::version_info::get() << std::endl;
}