#include <iostream>

// Module nhập liệu
int InputNumber() {
    int n;
    std::cout << "Nhap vao mot so nguyen khong am n: ";
    std::cin >> n;
    return n;
}

// Module tính toán
long long ComputeFactorial(int n) {
    if (n == 0)
        return 1;
    else
        return n * ComputeFactorial(n - 1);
}

// Module xuất kết quả
void OutputResult(long long result) {
    std::cout << "Giai thua cua n la: " << result << std::endl;
}

// Điều phối toàn bộ
void Factorial() {
    int n = InputNumber();
    if (n < 0) {
        std::cout << "Error: n phai la so nguyen khong am." << std::endl;
        return;
    }
    long long result = ComputeFactorial(n);
    OutputResult(result);
}

int main() {
    Factorial();
    return 0;
}