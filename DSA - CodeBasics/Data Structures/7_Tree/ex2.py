class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,level):
        if self.get_level() > level:
            return
        space = " " * self.get_level() * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_tree():

    Global = TreeNode("Global")

    Ind = TreeNode("India")
    
    Guj = TreeNode("Gujarat")
    Guj.add_child(TreeNode("Ahmedabad"))
    Guj.add_child(TreeNode("Baroda"))

    Kar = TreeNode("Karnataka")
    Kar.add_child(TreeNode("Bengaluru"))
    Kar.add_child(TreeNode("Mysore"))

    Ind.add_child(Guj)
    Ind.add_child(Kar)

    USA = TreeNode("USA")

    NJ = TreeNode("New Jersey")
    NJ.add_child(TreeNode("Princeton"))
    NJ.add_child(TreeNode("Trenton"))

    CF = TreeNode("California")
    CF.add_child(TreeNode("San Francisco"))
    CF.add_child(TreeNode("Mountain View"))
    CF.add_child(TreeNode("Palo Alto"))

    USA.add_child(NJ)
    USA.add_child(CF)

    Global.add_child(Ind)
    Global.add_child(USA)

    # Global.print_tree()
    return Global

if __name__ == '__main__':
    root = build_tree()
    root.print_tree(3)
