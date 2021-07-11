#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

int main() {
  srand((int) time(nullptr));
  int dice = (rand() % 6) + 1;
  cout << "Dice: " << dice << endl;
  return 0;
}
