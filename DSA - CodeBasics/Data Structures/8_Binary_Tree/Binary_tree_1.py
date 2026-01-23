class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self,val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def calculate_sum(self):
        sum = 0
        for i in self.in_order_traversal():
            sum += i
        return sum
            

    def in_order_traversal(self):
        element = []
        if self.left:
            element += self.left.in_order_traversal()

        element.append(self.data)

        if self.right:
            element += self.right.in_order_traversal()

        return element
    
    def pre_order_traversal(self):
        element = []

        element.append(self.data)

        if self.left:
            element += self.left.pre_order_traversal()

        if self.right:
            element += self.right.pre_order_traversal()

        return element
    
    def post_order_traversal(self):
        element = []

        if self.left:
            element += self.left.post_order_traversal()

        if self.right:
            element += self.right.post_order_traversal()

        element.append(self.data)

        return element
    
def build_tree(element):
    root = BinarySearchTreeNode(element[0])

    for i in element:
        root.add_child(i)

    return root

if __name__ == '__main__':

    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    element = [21,42,13,54,12,56,2]
    root_node = build_tree(element)

    print("In order traversal gives this sorted list:",root_node.in_order_traversal())
    print("Max :",root_node.find_max())
    print("Min :",root_node.find_min())
    print("Sum :",root_node.calculate_sum())
    print(root_node.pre_order_traversal())
    print(root_node.post_order_traversal())
    
