#include <iostream>
#include <vector>

int linear_search(const std::vector<int>& arr, int target) {
    for (size_t index = 0; index < arr.size(); ++index) {
        if (arr[index] == target) {
            return index;
        }
    }
    return -1;
}

int main() {
    std::vector<int> arr = {4, 2, 5, 1, 3};
    std::cout << linear_search(arr, 5) << std::endl; // Output: 2
    return 0;
}