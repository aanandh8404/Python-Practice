a = list(map(int,input("Enter values of array :").split()))
a.sort()
missing = []
for i in range(a[0],a[-1]+1):
    if i not in a:
        missing.append(i)
print(missing)