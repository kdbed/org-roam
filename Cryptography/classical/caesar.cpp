// caesar cipher encryption/decryption

#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

char caesar(char c, int k) // 'c' for letter and 'k' for key
{
  if(isalpha(c) && c != toupper(c))
  {
    c = toupper(c); // use upper to keep from using two alph. sets
    c = (((c - 65) + k)% 26) + 65; // encryption - (add k with c) mod 26 ;
                                   // 65 for ascii 'a'
  }
  else
  {
    c = ((((c - 65) - k ) + 26)%  26) + 65; // decryption
    c = tolower(c);
  }
  return c;
}


int main()
{
string input, output;
int choice = 0;

while (choice != 2) {
  cout<<endl<< "Press 1: Encryption/Decryption; Press 2: quit: ";

  try {
    cin >> choice;
    if (choice !=1 && choice != 2) throw "Incorrect Choice";
      }
  catch (const char* chc) {
    cerr<< "INCORRECT CHOICE!" << endl;
    return 1;
      }
  if (choice == 1){
    int key;
    try {
      cout<<endl<< "Choose key value (number between 1,26): ";
      cin >> key;
      cin.ignore();
      if (key < 1 || key > 26) throw "Incorrect key";
        }
    catch (const char* k) {
      cerr << "INCORRECT KEY VALUE CHOSEN!" << endl;
      return 1;
        }
    try {
      cout << endl << "Note: Put LOWER CASE letters for encryption and" << endl;
      cout << "UPPER CASE letters for decryption" << endl;
      cout << endl << "Enter ciphertext (alphabet chars only) and press enter: ";
      getline(cin, input);

      for (int i = 0; i < input.size(); i++) {
        if ((!(input[i] >= 'a' && input[i] <= 'z')) &&
            (!(input[i] >= 'A' && input[i] <= 'Z'))) throw "Incorrect string";
          }
      }
    catch (const char* str) {
      cerr << "Your string may have digits or special symbols!" << endl;
      cerr << "Please put only alphabet characters!" << endl;
      return 1;
      }

    for(unsigned int x = 0; x < input.length(); x++) {
      output += caesar(input[x], key);
    }

    cout << output << endl;
    output.clear();
  }

}
}
