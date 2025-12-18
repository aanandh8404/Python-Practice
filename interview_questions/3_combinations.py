# def combinations(arr, r, start=0, curr=[]):
#     if len(curr) == r:
#         print(curr)
#         return

#     for i in range(start, len(arr)):
#         combinations(arr, r, i + 1, curr + [arr[i]])

# arr = [1, 2, 3, 4]
# r = 3
# combinations(arr, r)


def combination(arr, r, start = 0, curr = []):
    res = []
    if len(curr) == r:
        res.append(curr)
    
    for i in range(start, len(arr)):
        combination(arr, r, i+1, curr + [arr[i]])
    return res

arr = [-1, 0, 1, 0, -2, 2]
r = 4
target = 0

result = combination(arr,r)
for i in result:
    if sum(i) == target:
        print(sorted(i))