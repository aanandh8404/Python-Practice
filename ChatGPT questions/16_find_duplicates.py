a = list(map(int,input("Enter number of array :").split()))
seen = []
duplicates = []
for i in a:
    if i in seen:
        duplicates.append(i)
    seen.append(i)
    
print(duplicates)