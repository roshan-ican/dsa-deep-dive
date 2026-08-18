from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# post order
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            depth = max(left, right) + 1
        return depth

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
    print("Max depth:", Solution().maxDepth(root))
 