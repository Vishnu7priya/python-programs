class Queue:
    def __init__(self):
        self.size=5
        self.queue=[0 for i in range(self.size)]
        self.front=-1
        self.rear=-1
    def enqueue(self,data):
        if self.rear==self.size-1:
            print("queue is full")
            return
        if self.front==-1:
            self.front=self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear+=1
            self.queue[self.rear]=data
    def isEmpty(self):
        return self.front==-1 or self.front>self.rear
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        self.front+=1
        print("front element is deleted")
    def display(self):
        if self.isEmpty():
            print("queue is empty")
            return
        print("The elements in the queue are:")
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=" ")
    def Front(self):
        if self.isEmpty():
            print("queue is empty")
            return
        print("\nFront is:")
        print(self.queue[self.front])
            
obj=Queue()
obj.enqueue(7)
obj.enqueue(2)
obj.enqueue(5)
obj.enqueue(6)
obj.enqueue(9)
obj.enqueue(1)
obj.display()
obj.Front()
obj.dequeue()
obj.dequeue()
obj.Front()
obj.display()

