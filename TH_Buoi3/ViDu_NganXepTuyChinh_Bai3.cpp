// custom_stack_cpp.cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Stack {
    private:
        vector<string> elements; // Su dung vector de luu tru phan tu
    public:
        // Them phan tu vao ngan xep
        void push(const string& item){
            elements.push_back(item);
            cout << "Da them " << item << " vao ngan xep" << endl;
        };

        // Loai bo phan tu khoi ngan xep
        void pop(){
            if(!isEmpty()){
                string item = elements.back();
                elements.pop_back();
                cout << "Da lay " << item << " ra khoi ngan xep" << endl;
            } else {
                cout << "Ngan xep rong!" << endl;
            };
        }

        // Xem phan tu o dinh ngan xep
        string peek() const {
            if (!isEmpty()){
                return elements.back();
            } else {
                throw out_of_range("Ngan xep rong!");
            }
        }

        // Kiem tra ngan xep rong
        bool isEmpty() const {
            return elements.empty();
        }

        // Tra ve kich thuoc ngan xep
        int size() const {
            return elements.size();
        }

        // In noi dung ngan xep tu dinh den day
        void display() const {
            cout << "Ngan xep (dinh den day): ";
            for (auto it = elements.rbegin(); it != elements.rend(); ++it)
                cout << *it << " ";
            cout << endl;
        }
};

// Ham main de minh hoa
int main(){
    Stack stack;
    stack.push("Sach A");
    stack.push("Sach B");
    stack.push("Sach C");
    stack.display(); // Output: Ngan xep (dinh den day): Sach C Sach B Sach A
    
    try{
    cout << "Phan tu o dinh ngan xep: " << stack.peek() << endl; // Output: Sach C
    } catch (const out_of_range& e){
        cout << e.what() << endl;
    }

    
    stack.pop();
    stack.display(); // Output: Ngan xep (dinh den day): Sach B Sach A
    
    cout << "Ngan xep co trong khong? " << (stack.isEmpty() ? "Co" : "Khong") << endl; // Output: Khong
    
    return 0;
}
