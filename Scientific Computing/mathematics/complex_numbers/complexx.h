/*********************************************************************** *
 * @file complexx.h                                                      *
 * @brief A header file that adds convenient extensions for complex nums *
 ************************************************************************/

#ifndef COMPLEXX_H
#define COMPLEXX_H

#include <complex>
using namespace std;

// Define C as abbreviation for complex<double>
typedef complex<double> C;

// Define i to be sqrt(-1), i.e., C(0.0, 1.0)
const C i = C{0.0, 1.0};

#endif
