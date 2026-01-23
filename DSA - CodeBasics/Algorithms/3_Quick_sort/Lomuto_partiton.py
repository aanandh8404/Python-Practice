def lomuto(elements,start,end):
    pivot = elements[end]
    i = p_index = start

    while p_index <= i and i < end:
        while elements[p_index] < pivot:
            p_index += 1
            i += 1

        while elements[i] > pivot:
            i += 1

        elements[p_index],elements[i] = elements[i],elements[p_index]
    return p_index

def quick_sort(elements,start,end):
    if start < end:
        p1 = lomuto(elements,start,end)
        quick_sort(elements,start,p1-1)
        quick_sort(elements,p1+1,end)

if __name__ == '__main__':
    # elements = [11,9,29,7,2,15,28]
    # quick_sort(elements,0,len(elements)-1)
    # print(elements)
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')