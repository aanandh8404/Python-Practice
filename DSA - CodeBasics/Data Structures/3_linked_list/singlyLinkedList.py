class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head == None :
            print("Linked List is Empty")
            return
        
        curr = self.head
        llstr = ''
        while curr:
            llstr += str(curr.val) + ' --> ' if curr.next else str(curr.val)
            curr = curr.next
        print(llstr)

    def get_length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def insert_at_start(self,val):
        node = Node(val,self.head)
        self.head = node

    def insert_at_end(self,val):
        node = Node(val,None)
        if self.head == None:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def insert_at(self, index, val):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_start(val)
            return
        
        count = 0
        curr = self.head
        while curr:
            if count == index - 1:
                node = Node(val,curr.next)
                curr.next = node
                break
            curr = curr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        curr = self.head

        while curr:
            if count == index - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            count += 1

    def insert_values(self,values):
        self.head = None
        for value in values:
            self.insert_at_end(value)

    def insert_after(self, after, val):
        curr = self.head
        while curr:
            if curr.val == after:
                node = Node(val,curr.next)
                curr.next = node
                break
            curr = curr.next

    def remove_by_value(self,val):
        count = 0
        curr = self.head
        while curr:
            if curr.val == val:
                self.remove_at(count)
                break
            curr = curr.next
            count += 1


ll = LinkedList()

# ll.insert_at_start(5)
# ll.insert_at_start(6)
# ll.insert_at_end(4)
# ll.insert_at(1,7)
# ll.insert_at(2,8)
# ll.remove_at(2)


ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after("mango","apple")
ll.print()
ll.remove_by_value("orange")
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()