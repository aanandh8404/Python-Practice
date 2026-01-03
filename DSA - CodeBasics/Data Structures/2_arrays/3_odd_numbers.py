# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function


n = int(input("Enter the number :"))
odd = []
for i in range(1,n):
    if i%2 != 0:
        odd.append(i)

print(odd)