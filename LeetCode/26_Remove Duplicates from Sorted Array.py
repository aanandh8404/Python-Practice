class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 1
        
        for i in range(1,len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k

obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))