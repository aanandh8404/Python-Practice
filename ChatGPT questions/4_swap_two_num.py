# method 1
# a = 10
# b = 15
# a,b = b,a
# print(a,b)

# method 2

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

a = a + b
b = a - b
a = a - b

print(a,b)