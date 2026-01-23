def shell_sort(arr):
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap,size):
            curr = arr[i]
            j = i
            while j >= gap and  arr[j-gap] > curr:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = curr
        gap = gap // 2

    arr = list(set(arr))
    return arr
        



if __name__ == "__main__":
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    print(shell_sort(elements))
    # print(elements)