class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
 
class Linked_list:
    def __init__(self):
        self.head=None
 
    def b_insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        newnode.next=self.head
        self.head=newnode
 
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            cur = self.head
            while cur:
                print(cur.data,end="->")
                cur=cur.next
 
    def end_insertion(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        cur = self.head
        while cur.next:
            cur=cur.next
        cur.next=newnode
 
    def del_beg(self):
        if self.head==None:
            print("empty list")
            return
        t=self.head
        self.head=self.head.next
        t.next=None
 
    def del_end(self):
        if self.head==None:
            print("empty list")
            return
        cur=self.head
        if self.head.next==None:
            self.head=None
            return
        while cur.next.next :
            cur=cur.next
        cur.next=None
 
    def insert_by_position(self,data,position):
        if position ==0:
            self.b_insert(data)
            return 
        newnode=Node(data)
        cur=self.head
        for i in range(position-1):
            if cur is None:
                print("position not found")
                break
            cur=cur.next
        else:
            newnode.next=cur.next
            cur.next=newnode
 
 
    def delete_by_position(self,position):
        if position ==0:
            self.del_beg()
            return 
        cur=self.head
        for i in range(position-1):
            if cur is None:
                print("position not found")
                break
            cur=cur.next
        else:
            cur.next=cur.next.next
 
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            cur = self.head
            while cur:
                print(cur.data,end="->")
                cur=cur.next

    def reverse_linkedlist(self):
        prev=None
        cur=self.head
        if self.head is None:
            print("Empty")
            return
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        self.head=prev
    def min_linkedlist(self):
        min=self.head.data
        cur=self.head.next
        while cur:
            if min>cur.data:
                min=cur.data
            cur=cur.next
        print(f"\nMin value:{min}")
        
 
obj=Linked_list()
obj.b_insert(8)
obj.b_insert(7)
obj.b_insert(4)
obj.b_insert(2)
obj.display()
print()
obj.insert_by_position(5,2)
obj.display()
print()
obj.reverse_linkedlist()
obj.display()
obj.min_linkedlist()
obj.del_beg()
obj.del_end()
obj.delete_by_position(1)
print()
obj.display()
obj.delete_by_position(0)
print()
obj.reverse_linkedlist()
