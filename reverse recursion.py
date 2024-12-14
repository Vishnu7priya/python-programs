def reverse(x,y=0):
    if x==0:
        return y
    else:
        d=x%10
        y=y*10+d
        return reverse(x//10,y)
n=int(input("Enter  the number:"))
print(reverse(n))