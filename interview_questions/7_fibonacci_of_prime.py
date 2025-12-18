
start,end = map(int,input("Enter start and end :").split())

a = 0
b = 1

res = []
for i in range(end+1):
    if i >= start:

        is_prime = True
        if a <= 1:
            is_prime = False
            
        for j in range(2,int(a**0.5)+1):
            if a%j == 0:
                is_prime = False
                break
        if is_prime:
            res.append(a)
        a,b = b , a+b

print("primes of fibonacci :",res)
print("sum of primes :", sum(res))
