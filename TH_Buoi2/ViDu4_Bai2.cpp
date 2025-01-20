#include <iostream>
#include <vector>
using namespace std;

// Ham tron hai mang con da duoc sap xep
void merge(vector<int> &arr, int left, int mid, int right) {
    int n1 = mid - left + 1; // So phan tu cua mang con 1
    int n2 = right - mid; // So phan tu cua mang con 2

    // Tao hai mang tam thoi
    vector<int> L(n1), R(n2);

    // Copy du lieu tu mang arr[] vao hai mang tam thoi
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Tron hai mang tam thoi lai
    int i = 0; // Chi so cua mang con 1
    int j = 0; // Chi so cua mang con 2
    int k = left; // Chi so cua mang sau khi tron

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy cac phan tu con lai cua L[] vao arr[]
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy cac phan tu con lai cua R[] vao arr[]
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Ham Merge Sort
void mergeSort(vector<int> &arr, int left, int right) {
    if (left < right) {
        // Tim diem chia de chia mang thanh hai nua
        int mid = left + (right - left) / 2;

        // Goi de quy de sap xep hai nua
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Tron hai nua
        merge(arr, left, mid, right);
    }
}   
int main() {
    vector<int> arr = {5, 2, 9, 1, 5, 6};
    mergeSort(arr, 0, arr.size() - 1);

    cout << "Ket qua Merge Sort: ";
    for (int x : arr)
        cout << x << " ";
    cout << endl;

    return 0;
}