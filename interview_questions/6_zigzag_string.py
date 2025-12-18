str = input("Enter a String :")
rows = int(input("Enter number of rows :"))

res = [""]*rows
r = 0
down = True

for ch in str:
    res[r] += ch

    if down:
        r += 1 
    else: 
        r -= 1

    if r == 0:
        down = True
    elif r == rows -1:
        down = False

print("".join(res))