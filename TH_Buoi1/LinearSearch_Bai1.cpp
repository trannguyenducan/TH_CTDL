#include <iostream>
#include <vector>

int LinearSearch(const std::vector<int>& A, int x) {
    for (size_t i = 0; i < A.size(); ++i) {
        if (A[i] == x) {
            return static_cast<int>(i);
        }
    }
    return -1; // Not found
}

int main() {
    std::vector<int> A = {3, 5, 2, 9, 1};
    int x = 9;
    int index = LinearSearch(A, x);
    if (index != -1) {
        std::cout << "Gia tri " << x << " duoc tim thay tai vi tri: " << index << std::endl;
    } else {
        std::cout << "Gia tri " << x << " khong ton tai trong mang." << std::endl;
    }
    return 0;
}