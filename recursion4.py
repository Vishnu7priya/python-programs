def fun(x,y):
    if x>y:
        return 0
    print(x)
    fun(x+1,y)
    if x!=y:
        print(x)
n,m=map(int,input("Enter the number:").split())
fun(n,m)