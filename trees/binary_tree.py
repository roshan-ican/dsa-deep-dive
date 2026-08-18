class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    # we considering start as root
    def pre_order_print(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal

    def in_order_print(self, start, traversal):
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.in_order_print(start.right, traversal)
        return traversal

    def post_order_print(self, start, traversal):
        if start:
            traversal = self.post_order_print(start.left, traversal)
            traversal = self.post_order_print(start.right, traversal)
            traversal += str(start.value) + "-"
        return traversal

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.in_order_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.post_order_print(tree.root, "")
        else:
            return False


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(8)


# pre-order traversal
print(tree.print_tree("preorder"))
# in-order traversal
print(tree.print_tree("inorder"))
# post order
print(tree.print_tree("postorder"))
