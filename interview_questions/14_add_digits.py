def add_digits(n):
    temp = 0
    for i in str(n):
        temp += int(i)

    if len(str(temp)) > 1:
        temp = add_digits(temp)
    return temp


num = int(input("Enter the number :"))
print(add_digits(num))