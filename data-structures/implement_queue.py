import sys
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = self.capacity - 1
        self.Q = [None] * self.capacity
        self.size = 0

    def enqueue(self, val):
        if self.size == self.capacity:
            print("overflow")

        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = val
        self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            print("empty")
            return
        val = self.Q[self.front]
        self.Q[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
    
    def peek(self):
        print("empty") if self.isEmpty() else print(self.Q[self.front])

    def isEmpty(self):
        return self.size == 0

if __name__ == "__main__":
    q = Queue(10)
    q.enqueue(1)
    q.enqueue(2)
    q.peek()
    print(q.Q)
    q.dequeue()
    print(q.Q)
    q.dequeue()
    print(q.Q)
    q.dequeue()
    print(q.Q)
