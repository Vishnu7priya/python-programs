n=int(input("Enter the no. of people:"))
l1=list(map(int,input("Enter the vote list:").split()))
l2=list(map(int,input("Enter the age list:").split()))
c=[0]*max(l1)
for i in range(n):
    if l2[i]>=18:
       c[l1[i]-1]+=1
temp=[]
temp=sorted(c,reverse=True)       
if temp[0]==temp[1]:
    print(-1)
else:
    print(c.index(temp[0])+1)

