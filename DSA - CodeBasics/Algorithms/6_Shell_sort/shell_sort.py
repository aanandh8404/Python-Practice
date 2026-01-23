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



if __name__ == "__main__":
    elements = [11,9,29,7,2,15,28]
    shell_sort(elements)
    print(elements)