class TreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,type):
        space = " " * self.get_level() * 3
        prefix = space + "|__" if self.parent else ""
        print(f"{prefix} {self.name if type == "name" else self.designation if type == "designation" else f"{self.name} ({self.designation})" if type == "both" else ""} ")
        if self.children:
            for child in self.children:
                child.print_tree(type)

    # def print_tree(self):
    #     space = " " * self.get_level() * 3
    #     prefix = space + "|__" if self.parent else ""
    #     print(f"{prefix}{self.name} ({self.designation})")
    #     if self.children:
    #         for child in self.children:
    #             child.print_tree()


def build_tree():

    CEO = TreeNode("Nilupul","CEO")

    CTO = TreeNode("Chinmay","CTO")

    IH = TreeNode("Vishwa","Infrastructure Head")
    IH.add_child(TreeNode("Dhaval","Cloud Manager"))
    IH.add_child(TreeNode("Abhijit","App Manager"))

    CTO.add_child(IH)
    CTO.add_child(TreeNode("Aamir","Application Head"))

    HR = TreeNode("Gels","HR Head")
    HR.add_child(TreeNode("Peter","Recruitment Manager"))
    HR.add_child(TreeNode("Waqas","Policy Manager"))

    CEO.add_child(CTO)
    CEO.add_child(HR)


    return CEO

if __name__ == '__main__':
    root = build_tree()
    root.print_tree("name")