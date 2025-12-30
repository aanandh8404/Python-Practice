def merge( nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1[:] = nums1[:m]
    nums1.extend(nums2)
    nums1.sort()
    print(nums1)

merge([1,2,3,0,0,0],3,[2,5,6], 3)




# def merge(nums1, m, nums2, n):
#     i = m - 1          # pointer for nums1 valid elements
#     j = n - 1          # pointer for nums2
#     k = m + n - 1      # pointer for placement in nums1

#     while j >= 0:
#         if i >= 0 and nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k -= 1
