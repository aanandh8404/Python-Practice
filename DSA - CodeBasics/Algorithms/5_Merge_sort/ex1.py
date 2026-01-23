def merge_sort(elements,key,descending = False):
    if len(elements) <= 1:
        return
    mid = len(elements)//2
    a = elements[:mid]
    b = elements[mid:]

    merge_sort(a,key,descending)
    merge_sort(b,key,descending)

    merge_sort_combine(a,b,elements,key,descending)

def merge_sort_combine(arr1,arr2,elements,key,descending):
    i = j = k = 0
    if descending:
        while i < len(arr1) and j < len(arr2):
            if arr1[i][key] > arr2[j][key]:
                elements[k] = arr1[i]
                k += 1
                i += 1

            else :
                elements[k] = arr2[j]
                k += 1
                j += 1
    else :
        while i < len(arr1) and j < len(arr2):
            if arr1[i][key] < arr2[j][key]:
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
    
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    merge_sort(elements,key='time_hours',descending=True)

    print(elements)