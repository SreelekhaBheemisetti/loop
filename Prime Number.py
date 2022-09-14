     # PRIME NUMBER
# i=1
# count=0
# user=int(input("enter the number:"))
# while i<=user:
#     if user%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print("prime number")
# else:
#     print("composite number")

# i=1
# user=int(input("enter the number:"))
# while i<=user:
#      j=1
#      count=0
#      while j<=i:
#           if i%j==0:
#                count=count+1
#           j=j+1
#      if count==2:
#           print(i)
#      i+=1



a=int(input("enter the a:"))
b=int(input("enter the b:"))
while a<=b:
     j=1
     count=0
     while j<=a:
          if a%j==0:
               count+=1
          j+=1
     if count==2:
          print(a)
     a+=1
          

     


