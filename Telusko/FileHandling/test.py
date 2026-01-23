# f = open('newFile.txt', 'x')

# for i in f:
#     a = i.split(" ")
#     for j in a:
#         print(j)
#         for k in j:
#             print(k)


with open("newfile.txt", 'r') as fp:
    data = fp.read()
    lines = data.split()
print(lines)
print(len(lines))