# method 1

# from itertools import combinations

# nums = list(map(int,input("Enter numbers of array :").split()))
# target = int(input("Enter target value :"))

# result = []

# combs = combinations(nums,r=4)
# for i in combs:
#     if sum(i) == target:
#         result.append(i)

# for i in result:
#     print(sorted(i))


# method 2

arr = list(map(int,input("Enter numbers of array :").split()))
target = int(input("Enter target value :"))


def combination(arr, r, start = 0, curr = []):
    if len(curr) == r:
        return [curr]
    res = []
    for i in range(start, len(arr)):
        res += combination(arr, r, i+1, curr + [arr[i]])
    return res

result = combination(arr,4)
for i in result:
    if sum(i) == target:
        print(sorted(i))