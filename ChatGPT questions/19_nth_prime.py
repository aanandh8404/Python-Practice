n = int(input("Enter the number of prime :"))

primes = []
def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

i = 2
while len(primes) < n:
    if isPrime(i):
        primes.append(i)
    i += 1

print(primes[n-1])