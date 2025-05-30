class graph:
    def __init__(self):
        self.size=4
        self.matrix=[[0 for i in range(self.size)] for i in range(self.size)]
        self.dict={"A":0,"B":1,"C":2,"D":3}
        
    def insert(self,v,e):
        i,j=self.dict[v],self.dict[e]
        self.matrix[i][j]=1
        self.matrix[j][i]=1

obj=graph()
obj.insert("A","B")
obj.insert("A","C")
obj.insert("B","D")
obj.insert("C","D")

for i in obj.matrix:
    print(i)
