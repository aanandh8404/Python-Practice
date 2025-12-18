n1 , n2 = map(int,input("Enter two numbers :").split())
a = []
b = []
for i in range(1,n1):
    if n1%i == 0:
        a.append(i)

for i in range(1,n2):
    if n2%i == 0:
        b.append(i)

if sum(a) == n2 and sum(b) == n1:
    print("Two number are amicable")
else:
    print("Two numbers are not amicable")