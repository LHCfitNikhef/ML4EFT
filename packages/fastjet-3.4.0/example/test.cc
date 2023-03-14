#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(){
    std::string input = "4 4.1 4";
    std::istringstream iss(input);
    int x;
    int y;
    double z;
    iss >> x >> y;
    cout << "x = " << x << endl << "y = " << y <<endl;
    return 0;
}
