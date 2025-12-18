nums = list(map(int,input("ENter values of Array :").split()))
k = int(input("Enter the subarray lenght :"))

left = 0
right = k
res = 0
for i in range(len(nums)):
    temp = nums[left:right]
    if len(temp) == k:
        avg = (sum(temp))/k
        if avg > res:
            res = avg
        left += 1
        right += 1

print(res)