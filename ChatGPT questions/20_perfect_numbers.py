start, end = map(int,input("Enter the start and end :").split())

for i in range(start, end+1):
    divisors = []
    for j in range(1,i):
        if i%j == 0:
            divisors.append(j)
    
    if sum(divisors) == i:
        print(i,end=" ")