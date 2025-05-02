class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def isEmpty(self):
        return len(self.__stack) ==0
    
    def isFull(self):
        return len(self.__stack) == self.__capacity
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Underflow")
        return self.__stack.pop()
    
    def push(self, value):
        if self.isFull():
            raise Exception("Overflow")
        
        self.__stack.append(value)

    def top(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.__stack[-1]
    
#example
stack1 = MyStack ( capacity =5)

stack1 . push (1)

stack1 . push (2)

print ( stack1 . isFull () )


print ( stack1 . top () )

print ( stack1 . pop () )

print ( stack1 . top () )

print ( stack1 . pop () )

print ( stack1 . isEmpty () )