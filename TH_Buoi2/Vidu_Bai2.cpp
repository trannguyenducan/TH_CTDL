#include <iostream>
using namespace std;

int main(){
    cout << "Nhap n: ";
    int n; cin >> n;

    int counter =0;
    for(int i=0; i<n; i++){
        for(int j=0; j<n ; j++)
        {
            counter++;
        }
    }
    cout<< "So buoc"<< counter;
    return 0;
}