#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>

#define LIMIT 25

static double getPi() {
    double pi = 18.85 / 6;
    return pi;
}

int main(int argc, const char *argv[])
{
    // one argument or exit
    if (argc == 1 || argc > 2) {
        std::cout << "Wrong number of args!" << std::endl;
        return -1;
    }

    int howMany = atoi(argv[1]);
    if (howMany > LIMIT) {
        std::cout << "Error! Limit is: " << LIMIT << std::endl; 
        return -1;
    }

    double pi = getPi();
    // std::ios::fixed - without this, howMany would be amount of all numbers
    // not just decimal point numbers
    // setprecision - set decimal precision
    std::cout << "Result for " << howMany << " is " << std::setiosflags(std::ios::fixed) 
              << std::setprecision(howMany) << pi << std::endl;

    return 0;
}
