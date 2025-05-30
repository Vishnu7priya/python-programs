class stack:
    def __init__(self):
        self.size=5
        self.stack=[0 for i in range(self.size)]
        self.top=-1
    def push(self,data):
        if self.top==self.size-1:
            print("overflow")
        else:
            self.top+=1
            self.stack[self.top]=data
    def display(self):
        if self.top==-1:
            print("underflow")
        else:
            print("The elements in the stack are:")
            for i in range(self.top,-1,-1):
                print(self.stack[i])
    def pop(self):
        if self.top==-1:
            print("underflow")
        else:
            self.top-=1
            print("Top element is popped")
            return self.stack[self.top+1]
            
    def peek(self):
        if self.top==-1:
            print("underflow")
        else:
            print("Top element is:")
            print(self.stack[self.top])
            
obj=stack()
obj.push(7)
obj.push(1)
obj.push(5)
obj.push(4)
obj.push(2)
obj.push(8)
obj.display()
obj.peek()
obj.pop()
obj.display()
        
        
