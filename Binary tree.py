class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

root=Node(7)
root.left=Node(5)
root.right=Node(10)
root.left.left=Node(22)
root.left.right=Node(18)
root.right.left=Node(45)
root.right.right=Node(30)
