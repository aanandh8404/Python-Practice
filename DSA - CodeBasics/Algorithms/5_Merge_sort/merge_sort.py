def merge_sort(elements):
    if len(elements) <= 1:
        return
    mid = len(elements)//2
    a = elements[:mid]
    b = elements[mid:]

    merge_sort(a)
    merge_sort(b)

    merge_sort_combine(a,b,elements)

def merge_sort_combine(arr1,arr2,elements):
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            elements[k] = arr1[i]
            k += 1
            i += 1
        
        else :
            elements[k] = arr2[j]
            k += 1
            j += 1

    while i < len(arr1):
        elements[k] = arr1[i]
        k += 1
        i += 1

    while j < len(arr2):
        elements[k] = arr2[j]
        k += 1
        j += 1
    

if __name__ == '__main__':
    
    # a = [5,8,12,56,62,65]
    # b = [7,9,45,51]

    elements = [10, 3, 15, 7, 8, 23, 98, 29]
    # merge_sort_combine(a,b,elements)
    merge_sort(elements)

    print(elements)