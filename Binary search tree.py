class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
class Tree:
    def __init__(self):
        self.root=None
 
    def insert(self,data):
        self.root=self.rec_insert(self.root,data)
 
    def rec_insert(self,root,data):
        if root is None:
            return Node(data)
        if root.data<data:
            root.right=self.rec_insert(root.right,data)
        else:
            root.left=self.rec_insert(root.left,data)
        return root
 
 
    def inorder_traversal(self,root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data,end=" ")
            self.inorder_traversal(root.right)
    def preorder_traversal(self,root):
        if root is not None:
            print(root.data,end=" ")
            self.inorder_traversal(root.left)
            self.inorder_traversal(root.right)
    def postorder_traversal(self,root):
        if root is not None:
            self.inorder_traversal(root.left)
            self.inorder_traversal(root.right)
            print(root.data,end=" ")

    def Min(self):
        if self.root==None:
            print("EMPTY")
            return
        cur=self.root
        while cur.left:
            cur=cur.left
        print(f"{cur.data}")

    def Max(self):
        if self.root==None:
            print("EMPTY")
            return
        cur=self.root
        while cur.right:
            cur=cur.right
        print(f"{cur.data}")

    def max(self,root):
        cur = root
        while cur.right:
            cur=cur.right
        return cur.data
        
    def delete(self,data):
        self.root=self.rec_deletion(self.root,data)
    def rec_deletion(self,root,key):
        if root is None:
            return None
        
        if root.data<key:
            root.right=self.rec_deletion(root.right,key)
        elif root.data>key:
            root.left=self.rec_deletion(root.left,key)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            max = self.max(root.left)
            root.data=max
            root.left = self.rec_deletion(root.left,max)
        return root
    def level_order_traversal(self):
 
        queue = [self.root] # 
        res = []  # [20]  [10,27]
        while queue:
            sub=[] # 10 27
            for i in range(len(queue)): # 2
                temp = queue.pop(0) # 27
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                sub.append(temp.data)
            res.append(sub)
        return res
            

    
 
obj=Tree()
obj.insert(20)
obj.insert(10)
obj.insert(7)
obj.insert(27)
obj.insert(34)
obj.insert(3)
obj.insert(9)
obj.insert(25)
obj.insert(18)
print("Inorder traversal is:")
obj.inorder_traversal(obj.root)
print()
print("Preorder traversal is:")
obj.preorder_traversal(obj.root)
print()
print("Postorder traversal is:")
obj.postorder_traversal(obj.root)
print()
print("Min value is:")
obj.Min()
print("Max value is:")
obj.Max()
print()
obj.delete(10)
obj.inorder_traversal(obj.root)
print()
obj.delete(34)
obj.inorder_traversal(obj.root)
print()
print(obj.level_order_traversal())
