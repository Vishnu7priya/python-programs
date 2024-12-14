def prime(x,y=2):
    if x<=1:
        return 0
    if x==2:
        return 1
    if x%y==0:
        return 0
    if y*y>x:
        return 1
    return prime(x,y+1)
n=int(input("Enter a number:"))
t=prime(n)
if t==1:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")