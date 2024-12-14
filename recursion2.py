def fun(n):
    if n==0:
        return 0
    if n%2!=0:
        print(n)
    fun(n-1)
    if n!=1 and n%2!=0:
        print(n)
x=int(input("Enter the number:"))
fun(x)