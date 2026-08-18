from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# post order
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.height(root)
        return self.diameter

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        self.diameter = max(self.diameter, left + right)
        return max(left, right) + 1
            


# Input: root = [1,null,2,3,4,5]

# Output: 3


def build_tree(values: list):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def print_tree(root: Optional[TreeNode], prefix="", is_left=True):
    if not root:
        print(prefix + ("└── " if is_left else "┌── ") + "None")
        return
    print(prefix + ("└── " if is_left else "┌── ") + str(root.val))
    print_tree(root.left, prefix + ("    " if is_left else "│   "), True)
    print_tree(root.right, prefix + ("    " if is_left else "│   "), False)


if __name__ == "__main__":
    root = build_tree([1, None, 2, 3, 4, 5])
    print_tree(root)
    print("Diameter:", Solution().diameterOfBinaryTree(root))
