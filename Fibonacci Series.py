# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8.... The first two terms are 0 and 1.
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series : ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b
