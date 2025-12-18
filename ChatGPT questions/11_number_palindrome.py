n = int(input("Enter a number :"))

temp = n
rev = 0

while temp > 0:
    digit = temp %  10
    rev = rev * 10 + digit
    temp //= 10

print("palindrom" if n == rev else "Not palindrome")
