def add_digits(n):
    temp = n
    if len(str(temp)) == 1:
        for i in str(n):
            temp += int(i)


n = int(input("Enter the number :"))