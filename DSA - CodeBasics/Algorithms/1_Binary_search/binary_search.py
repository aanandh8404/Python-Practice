
def binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            start = mid + 1

        elif arr[mid] > target:
            end = mid - 1

    return -1

def binary_search_recursion(arr,t,start, end):
    if start >= end:
        return -1
    
    mid = (start + end) // 2

    if mid >= len(arr) or mid < 0:
        return -1

    if arr[mid] == t:
        return mid
    
    elif arr[mid] < target:
        start = mid + 1

    elif arr[mid] > target:
        end = mid - 1

    return binary_search_recursion(arr,t,start,end)
    

if __name__ == '__main__':
    arr = [1,3,6,8,12,15,19,23,45,67]
    target = 1

    print("Found at :",binary_search(arr,target))
    print("Found at :",binary_search_recursion(arr,target,0,len(arr)))
