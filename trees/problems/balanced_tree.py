# Given a binary tree, return true if it is height-balanced and false otherwise.

# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# root = [1, 2, 3, null, null, 4] ->>true

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# post order
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if node is None:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


# Input: root = [1,2,3,null,null,4]
# Output: 3


def build_tree(values: list, index=0):
    if index >= len(values) or values[index] is None:
        return None
    node = TreeNode(values[index])
    node.left = build_tree(values, 2 * index + 1)
    node.right = build_tree(values, 2 * index + 2)
    return node


def print_tree(root: Optional[TreeNode], prefix="", is_left=True):
    if not root:
        print(prefix + ("└── " if is_left else "┌── ") + "None")
        return
    print(prefix + ("└── " if is_left else "┌── ") + str(root.val))
    print_tree(root.left, prefix + ("    " if is_left else "│   "), True)
    print_tree(root.right, prefix + ("    " if is_left else "│   "), False)


if __name__ == "__main__":
    root = build_tree([1, 2, 3, None, None, 4])
    print_tree(root)
    print("Max depth:", Solution().isBalanced(root))
 