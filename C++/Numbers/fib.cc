#include <iostream>
#include <cstdlib>

using std::cout;
using std::endl;

static int *fib(int arg) {
    int *rv = new int[arg];
    int i = 0;
    if (rv == NULL) {
        return NULL;
    }

    for (i = 0; i < arg; i++) {
        rv[i] = 0;
    }

    for (i = 0; i < arg; i++) {
        if (i == 0 || i == 1) {
            rv[i] = 1;
            continue;
        }
        rv[i] = rv[i-1] + rv[i-2];
    }

    return rv;
}

int main(int argc, char *argv[])
{
    int *rv = NULL;
    int i = 0, howMany = 0;
    if(argc == 1 || argc > 2) {
        cout << "Wrong number of arguments!" << endl;
        return 1;
    }
    
    howMany = atoi(argv[1]);
    if (howMany == 0) {
        cout << "Wrong argument!" << endl;
        return 2;
    }

    rv = fib(howMany);
    if (rv == NULL) {
        return 3;
    }

    for (i = 0; i < howMany; i++) {
        cout << "Element #" << i << ": " << rv[i] << endl;
    }
    
    delete []rv;
    return 0;
}
