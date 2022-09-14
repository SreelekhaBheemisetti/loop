# perfect number, a positive integer that is equal to the sum of its proper divisors


# i=1
# sum=0
# user=int(input("enter the number:"))
# temp=user
# while i<user:
#     if temp%i==0:
#         sum=sum+i
#     i=i+1
# if sum==user:
#         print("pefect number")
# else:
#     print("not perfect number")
 
# Print From 1-100

a=int(input("enter the a:"))
b=int(input("enter the b:"))
while a<=b:
    i=1
    sum=0
    while i<a:
        if a%i==0:
            sum=sum+i
        i=i+1
    if sum==a:
        print(sum, end=" ")
    a+=1

