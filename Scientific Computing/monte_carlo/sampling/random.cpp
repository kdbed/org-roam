// generate a sequence of random numbers, uniformly distributed in the interval
// [-1, +1) ; uses drand48() with default seed = 1


#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <fstream>
#include <iomanip>

using namespace std;

int main() {
  cout.precision(6);
  cout.setf(ios::fixed | ios::showpoint);

  int i, n;
  double x, rand, I, stder, f_val, f_val2;

  static int first_time = 1;
  static ofstream f_data;

  /// open file
  //
  if (first_time)
  {
    f_data.open("data.txt");
    if (f_data.bad())
    {
      cout << "Failed to open data file.\n" << flush;
    }
    first_time = 0;
  }

  /// get sample points
  //

  cout << "Number of sample points" << endl;
  cin >> n;

  f_val   = 0.0;
  f_val2  = 0.0;

 for (i = 1; i <= n; i++)
 {
  rand = drand48(); // random num [0,1]
  //  default seed is 1
  x = 2.0 * (rand - 0.5);
  f_data << i << "\t" << x << endl;

  f_val = x;
  f_val2 = f_val2 + x*x;
 }

I = f_val*2.0/n;

/// eval standard error

f_val = f_val/n;
f_val2 = f_val2/n;

stder = 2.0*sqrt((f_val2 - f_val*f_val)/n);

cout << setw (8) << n << setw (12) << I << setw(12) << stder << endl;

return 0;
}
