def minimumPairRemoval(nums):
        res = 0
        n = len(nums)
        for i in range(n-2):
            if nums[i] <= nums[i+1]:
                continue
            
            nums[i+1] = nums[i+1]+nums[i+2]
            # nums.remove(nums[i+1])
            nums[i+2] , nums[n-1] = nums[n-1], nums[i+2]
            res += 1
        return res

nums = [5,2,3,1]
print(minimumPairRemoval(nums))