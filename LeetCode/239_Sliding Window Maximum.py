from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):

        temp = deque(nums[0:k])
        res = []
        for i in range(k,len(nums)+1):
            maxi = max(temp)
            res.append(maxi)
            if i < len(nums):
                temp.append(nums[i])
            temp.popleft()
        return res

obj = Solution()
print(obj.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))







        # left = 0
        # right = k
        # res = []
        # for i in range(len(nums)-(k-1)):
        #     maximum = max(nums[left:right])
        #     res.append(maximum)
        #     left += 1
        #     right += 1
        # return res