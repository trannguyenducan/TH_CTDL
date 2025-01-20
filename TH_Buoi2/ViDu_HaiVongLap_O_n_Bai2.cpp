#include <iostream>

void printPairs(int n) {
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            std::cout << "(" << i << ", " << j << ")" << std::endl;
        }
    }
}

int main() {
    printPairs(3);
    return 0;
}