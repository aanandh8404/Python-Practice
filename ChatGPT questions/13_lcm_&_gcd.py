n1,n2 = map(int,input("Enter two number :").split())

temp1,temp2 = n1,n2

while temp2 > 0:
    temp1, temp2 = temp2, temp1 % temp2
gcd = temp1

lcm = n1*n2 // gcd
print(gcd)
print(lcm)