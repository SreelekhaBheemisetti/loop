n=int(input("enter the number:"))
i=1
while i<=n:
    if i%2!=0:
        print(i,end=" ")
    if i%10==0:
        print()
    i+=1