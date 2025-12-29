# class Solution:
#     def twoSum(self, nums, target):
#         temp = []
#         seen = {}
#         for i in range(len(nums)):
#             diff = target - nums[i]

#             if diff in seen:
#                 temp.append(seen[diff])
#                 temp.append(i)

#             seen[nums[i]] = i
#         return temp

# nums = list(map(int,input("Enter numbers of array :").split()))
# target = int(input("Enter target value :"))

# obj = Solution()
# result = obj.twoSum(nums,target)

# print(result)




nums = list(map(int,input("Enter numbers of array :").split()))
target = int(input("Enter target value :"))

seen = {}

for i,num in enumerate(nums):
    compliment = target - num
    if compliment in seen:
        print([seen[compliment],i])
        break
    seen[num] = i
