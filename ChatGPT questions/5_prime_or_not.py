a = int(input("Enter a number :"))

is_prime = True
if a <= 1:
    is_prime = False
else :
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            is_prime = False
            break
print("is Prime :",is_prime)