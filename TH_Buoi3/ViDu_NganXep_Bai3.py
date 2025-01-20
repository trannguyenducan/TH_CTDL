#stack_python.py
import sys
sys.stdout.reconfigure(encoding='utf-8')

class Stack:
    def __init__(self):
        self.elements = [] # Su dung list de luu tru cac phan tu
    def push(self, item):
        self.elements.append(item) # Them phan tu vao cuoi ngan xep
        print("Đã thêm phần tử '{item}' vào ngăn xếp")
    def pop(self):
        if not self.isEmpty():
            item = self.elements.pop() # Loai bo phan tu cuoi cung khoi ngan xep
            print("Đã lấy '{item}' khỏi ngăn xếp")
            return item
        else:
            print("Ngăn xếp rỗng")
            return None
    def peek(self):
        if not self.isEmpty():
            return self.elements[-1] # Lay phan tu cuoi cung cua ngan xep
        else:
            print("Ngăn xếp rỗng")
            return None
    def isEmpty(self):
        return len(self.elements) == 0 # Kiem tra xem danh sach co rong hay khong
    def size(self):
        return len(self.elements) # Tra ve kich thuoc ngan xep
    def display(self):
        print("Ngăn xếp (từ đỉnh đến đáy):", self.elements[::-1]) # In ngan xep tu dinh den day

# Minh hoa su dung ngan xep
if __name__ == "__main__":
    stack = Stack()
    stack.push("Sách A")
    stack.push("Sách B")
    stack.push("Sách C")
    stack.display() # Output: Ngăn xếp (đỉnh đến đáy): ['Sách C', 'Sách B', 'Sách A']

    top_item = stack.peek()
    print("Phần tử đầu ngăn xếp:", top_item) # Output: Phần tử đầu ngăn xếp: Sách C 

    stack.pop()
    stack.display() # Output: Ngăn xếp (đỉnh đến đáy): ['Sách B', 'Sách A']

    print("Ngăn xếp có trống không?", stack.isEmpty()) # Output: False