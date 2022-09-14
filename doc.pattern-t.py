    #     *
    #    * *
    #   * * *
    #  * * * *
    # * * * * *   

# n=int(input("enter the number:"))
# i=0
# while i<n:
#     j=n-i-1
#     while j>0:
#         print(end=" ")
#         j=j-1
#     k=i+1
#     while k>0:
#         print("*", end=" ")
#         k=k-1
#     i=i+1
#     print()


# n=int(input("enter the number:"))
# for i in range(1,n):
#     for j in range(n-i,0,-1):
#         print(" ",end=" ")
#     for k in range(0,i):
#         print("*",end="   ")
#     print()

n=int(input("enter the number:"))
i=1
while i<=n:
    j=n
    while j>=n-i:
        print(" ", end=" " )
        j=j-1
    k=n
    while k>=i:
         print(" * ",end=" ")
         k=k-1
    print()
    i+=1

# n=int(input("enter the number:"))
# for i in range(n,0,-1):
#     for j in range(0,n-i):
#         print(end=" ")
#     for j in range(0,i):
#         print("*", end=" ")
#     print()



