def bubble_sort(arr,key=None):
    size = len(arr)

    for i in range(size - 1):

        swapped = False
        for j in range(size - 1 - i):
            if arr[j][key] > arr[j+1][key]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        
        if not swapped:
            break

if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3,4,2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort(elements,key='name')
    print(elements)