# an integer number divisible by the sum of its digit in base 


# sum=0
# user=int(input("enter the number:"))
# a=user
# while user>0:
#     r=user%10
#     sum=sum+r
#     user=user//10
# if a%sum==0:
#     print("harshad number")
# else:
#     print("not a harshad number")



# a=int(input("enter the a:"))
# b=int(input("enter the b:"))
# while a<b:
#     n=a
#     b=n
#     sum=0
#     while n>0:
#         r=n%10
#         sum=sum+r
#         n=n//10
#     if b%sum==0:
#         print(b, end="")
#     a=a+1

for i in range(50,101):
    a=i
    sum=0
    while i>0:
        digit=i%10
        sum=sum+digit
        i=i//10
    if a%sum==0:
        print(a, end=",")



a=50
while a<100:
    a=i
    sum=0
    # i=50
    while i>0:
        digit=i%10
        sum=sum+digit
        i=i//10
    if a%sum==0:
        print(a, end=" ")



