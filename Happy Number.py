# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.


n=int(input("enter the number:"))
a=n
while a>=10:
    sum=0 
    while a>0:
        r=a%10
        sum=sum+r**2
        a=a//10
    a=sum
if a==1:
    print("happy number")
else:
    print("unhappy")
