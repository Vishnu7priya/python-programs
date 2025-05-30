class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Double_linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def begin_insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=self.tail=newnode
            return
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
    def end_insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=self.tail=newnode
            return
        newnode.prev=self.tail
        self.tail.next=newnode
        self.tail=newnode
    def forward_display(self):
        if self.head is None:
            print("\nEmpty")
            return
        cur=self.head
        print("\nForward display:")
        while cur:
            print(cur.data,end="->")
            cur=cur.next
    def backward_display(self):
        if self.head is None:
            print("\nEmpty")
            return
        cur=self.tail
        print("\nBackward display:")
        while cur:
            print(cur.data,end="->")
            cur=cur.prev
    def begin_delete(self):
        if self.head is None:
            print("is Empty")
            return
        if self.head.next is None:
            self.head=self.tail=None
            return
        self.head=self.head.next
        self.head.prev.next=None
        self.head.prev=None
    def end_delete(self):
        if self.head is None:
            print("is Empty")
            return
        if self.head.next is None:
            self.head=self.tail=None
            return
        self.tail=self.tail.prev
        self.tail.next.prev=None
        self.tail.next=None
    def delete_by_data(self,key):
        if self.head is None:
            print("Empty")
            return
        if self.head.data==key:
            self.begin_delete()
            return
        if key == self.tail.data:
                self.end_delete()
                return
        cur = self.head
        while cur and cur.data!=key:
            cur=cur.next
        if cur:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.prev=cur.next=None 
        else:
            print("\nno data found")

            

obj=Double_linkedlist()
obj.end_delete()
obj.begin_insert(7)
obj.begin_insert(5)
obj.forward_display()
obj.backward_display()
obj.begin_delete()
obj.end_insert(2)
obj.end_insert(4)
obj.forward_display()
obj.backward_display()
obj.begin_delete()
obj.forward_display()
obj.backward_display()
obj.delete_by_data(2)
obj.forward_display()
obj.delete_by_data(7)
obj.delete_by_data(4)
obj.forward_display()



