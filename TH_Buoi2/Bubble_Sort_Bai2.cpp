#include <iostream>
#include <vector>
using namespace std;

// Hàm Bubble Sort
void BubbleSort(vector<int> &arr)
{
    int n = arr.size();
    for (int i = 0; i < n - 1; i++)
    {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped)
            break;
    }
}  
int main()
{
    vector<int> arr = {5, 2, 9, 1, 5};
    BubbleSort(arr);
    cout << "Ket qua sau Merge Sort: ";
    for (int x : arr)
    cout << x << " ";
    cout << endl;
    return 0;
}