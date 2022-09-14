# n=int(input("enter the number"))
i=0
while i<5:
    j=5-i-1
    while j>0:
        print(end=" ")
        j-=1
    k=i+1
    while k>0:
        print("*",end=" ")
        k-=1
    i+=2
    print()
# n=int(input("enter the number:"))
i=1
while i<=3:
    j=3
    while j>=3-i:
        print(end=" ")
        j=j-1
    k=3
    while k>=i:
         print("*",end=" ")
         k=k-1
    print()
    i+=2