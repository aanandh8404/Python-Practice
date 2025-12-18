# rows = int(input("Enter a Number :"))

# for i in range(1,rows+1):
#     for space in range(rows-i,0,-1):
#         print(end=" ")

#     num = 1
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num = int(num*(i - j)/j)
#     print("")


# method 2

n = int(input("Enter number of rows :"))
a = [1]
temp = []
res = []
for i in range(n):
    res.append(a)
    temp.append(1)

    for j in range(len(a)-1):
        temp.append(a[j]+a[j + 1])
    temp.append(1)

    a = temp
    temp = []

# 1
# for i in res:
#     print(i)


# 2
# for i in range(len(res)):
#     for j in range(len(res)-i,0,-1):
#         print(end=" ")

#     print(res[i])


# 3
for i in range(len(res)):
    for j in range(len(res)-i,0,-1):
        print(end=" ")

    for j in res[i]:
        print(j,end=" ")
    print()