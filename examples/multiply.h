#pragma once

#include <iostream>

// function definition for a generic method for multiplying numbers
template <typename T>
T multiply(T a, T b) {
    T result = a * b;
    std::cout << "Inside C++: " << result << std::endl;
    
    return result;
}

