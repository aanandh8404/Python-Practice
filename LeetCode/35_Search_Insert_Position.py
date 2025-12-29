def searchInsert(nums, target) -> int:
    n = len(nums)
    low = 0
    high = n-1
    
    while(low<=high):
        mid = (high+low)//2
        if nums[mid] ==  target:
            return mid
        elif nums[mid]<target:
            low = mid +1
        else:
            high = mid -1
    return high + 1

print(searchInsert([1,3,5,6],2))