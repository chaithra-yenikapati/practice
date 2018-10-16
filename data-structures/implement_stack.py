class Stack:
    def __init__(self):
        self.S = [None]*10
        self.top = -1
        self.capacity = 10
    def push(self, val):
        if(self.top == self.capacity - 1):
            print("overflow")
            return
        self.top += 1
        self.S[self.top] = val

    def pop(self):
        if self.top < 0:
            print("empty")
            return
        print(self.S[self.top])
        self.S[self.top] = None
        self.top -= 1

    def peek(self):
        if self.top < 0:
            print("empty")
            return
        
        return(self.S[self.top])
    
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    print(s.peek())
    for i in range(3, 11):
        s.push(i)
    print(s.S)
    s.push(11)
