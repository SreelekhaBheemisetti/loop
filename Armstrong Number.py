num=int(input("enter the number:"))
a=len(str(num))
sum=0
temp=num
while temp>0:
    b=temp%10
    sum=b**a+sum
    temp=temp//10
if num==sum:
    print("armstrong number")
else:
    print("not an armstrong number")



