print("Square Root Approximation using Heron's Algorithm")
print("Programmed by Sandra Tang")
print()

num = input("What number do you want to find the square root of?")
num = int(num)

x = 1
product = x * x

while not abs(product - num) < 0.000001:
  x = (x + (num/x))/2
  product = x * x

num = str(num)
x = str(x)
product = str(product)

print()
print ("The square root of " + num + " is approximately " + x + ".")
print (x + " * " + x + " = " + product)
