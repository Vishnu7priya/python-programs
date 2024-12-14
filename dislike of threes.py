t=int(input("Enter the test cases:"))
for i in range(t):
    k=int(input("Enter the numbers:"))
    count=0
    i=1
    while(1):
        if i%3!=0 and i%10!=0:
            count+=1
            if count==k:
                print(i)
                break
        i+=1 