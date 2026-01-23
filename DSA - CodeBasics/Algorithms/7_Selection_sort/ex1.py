def selection_sort(arr,key):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i,len(arr)):
            if arr[j][key[0]] < arr[min_index][key[0]]:
                min_index = j
            if arr[j][key[0]] == arr[min_index][key[0]]:
                if arr[j][key[1]] < arr[min_index][key[1]]:
                    min_index = j
        if i != min_index:
            arr[i],arr[min_index] = arr[min_index],arr[i]

if __name__ == '__main__':
    elements = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    selection_sort(elements,key=['First Name','Last Name'])
    print(elements)