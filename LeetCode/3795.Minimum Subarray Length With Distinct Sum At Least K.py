# You are given an integer array nums and an integer k.

# Return the minimum length of a subarray whose sum of the distinct values present in that subarray (each value counted once) is at least k. If no such subarray exists, return -1.


def minLength(nums, k):
        last_seen = {}
        start = 0
        window_sum = 0
        min_len = -1
        for i,num in enumerate(nums):
            while num in last_seen and last_seen[num] >= start:
                    window_sum -= nums[start]
                    start = last_seen[num] + 1

            last_seen[num] = i
            window_sum += num

            while window_sum >= k:
                curr_len = i+1 - start
                min_len = curr_len if min_len == -1 else min(min_len,curr_len)
                window_sum -= nums[start]
                start += 1

        return min_len


n = [18,18,19,19,21,22]
k = 39
print(minLength(n,k))







# min_len = -1
        # start = 0
        # end = 1
        # for i in range(len(nums)):
        #     curr_arr = nums[start:end]
        #     if sum(set(curr_arr)) >= k:
        #         curr_len = end - start
        #         if curr_len < min_len:
        #              start += 1
        #         if min_len == -1:
        #             min_len = curr_len
        #         else:
        #             min_len = min(min_len,curr_len)
        #             start += 1

        #     else:
        #         end += 1
        # return min_len











# min_len = -1
        # # start = 0
        # # end = 
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         curr_sub = nums[i:j]
        #         if sum(curr_sub) >= k:
        #             curr_len = j - i
        #             min_len = curr_len if min_len == -1 else min(min_len,curr_len)
        # return min_len