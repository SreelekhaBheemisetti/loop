# * * * * *
# * * * *
# * * *
# * *
# *
n=int(input("enter the number:"))
i=n
while i>=1:
    j=1
    while j<=i:
        print("*", end=" ")
        j=j+1
    print()
    i=i-1


# n=int(input("enter the number:"))
# for i in range(n+1,1,-1):
#     for j in range(1,i,1):
#         print("*", end=" ")
#     print()