def threeSum(nums):
        d = {}
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            compliment = 0 - nums[i]
            d[compliment] = i

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[j] + nums[k]

                if total < compliment:
                    j += 1
                
                elif total > compliment:
                    k -= 1
                elif total in d:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j] ==  nums[j-1] and j < k:
                        j += 1
        return res



        # res = []
        # nums.sort()

        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
                
        #     j = i + 1
        #     k = len(nums) - 1

        #     while j < k:
        #         total = nums[i] + nums[j] + nums[k]

        #         if total < 0:
        #             j += 1

        #         elif total > 0:
        #             k -= 1

        #         else:
        #             res.append([nums[i],nums[j],nums[k]])
        #             j += 1

        #             while nums[j] == nums[j-1] and j < k:
        #                 j += 1
        # return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))