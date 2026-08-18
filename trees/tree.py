class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level=0):
        indent = " " * level * 4
        print(f"{indent}Level {level}: {self.data}")
        for child in self.children:
            child.print_tree(level + 1)


def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    mobile = TreeNode("Mobile")

    root.add_child(laptop)
    root.add_child(mobile)

    laptop.add_child(TreeNode("MacBook"))
    laptop.add_child(TreeNode("ThinkPad"))
    mobile.add_child(TreeNode("iPhone"))
    mobile.add_child(TreeNode("Pixel"))

    return root


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
