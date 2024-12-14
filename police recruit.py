n=int(input("Enter the no of events"))
events=list(map(int,input("Enter the list of events:").split()))
free_off=0
untreated=0
for i in events:
    if i==-1:
        if free_off>0:
            free_off-=1
        else:
            untreated+=1
    else:
        free_off+=i

print(untreated)
