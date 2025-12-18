a,b,c = map(int,input("enter three number :").split())
print(a if a>b and a>c else b if b>a and b>c else c )