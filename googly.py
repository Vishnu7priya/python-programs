n=int(input("Enter the num:"))
count=0
for i in range(len(str(n))):
    digit=n%10
    count=count+digit
    n=n//10
flag=0
for j in range(2,count):
    if count%j==0:
        flag=1
        break
if flag==1:
    print("Not GOOGLY")
else:
    print("GOOGLY")