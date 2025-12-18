n = int(input("Enter a number :"))

num = 0
digit = len(str(n))
for i in str(n):
    num += int(i)**digit
print("Amstrong" if num == n else "Not Armstrong")
# print(len(str(n)))