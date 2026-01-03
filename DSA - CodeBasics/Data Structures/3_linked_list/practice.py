class SinglyNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)

Head.next = A
A.next = B
B.next = C

# print(Head)

def display(head):
    curr = head
    arr = []
    while curr:
        arr.append(str(curr))
        curr = curr.next

    print(" -> ".join(arr))

display(Head)


def search(head,val):
    curr = head
    while curr:
        if curr.val == val:
            return True
        curr = curr.next
    return False

print(search(Head,4))

def insert_on_start(head,val):
    curr = SinglyNode(val,head)

    while curr:
        print(curr.val)
        curr = curr.next

insert_on_start(Head, 10)
insert_on_start(Head, 12)