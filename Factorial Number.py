i=1
product=1
user=int(input("enter the number:"))
while i<=user:
    if user>=i:
        product=product*i
    i=i+1
print(product)