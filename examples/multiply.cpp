#include "multiply.h"

// in the implementation file we explicitly allow to use the int and double 
// version of our generic multiply function (definition imported via #include)
template int multiply<int>(int a, int b);
template double multiply<double>(double a, double b);

