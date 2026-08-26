# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:

        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2

            node = TreeNode(nums[mid])

            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)

            return node

        return build(0, len(nums) - 1)


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
    nums = [-10, -3, 0, 5, 9]
    root = Solution().sortedArrayToBST(nums)
    print_tree(root)


# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
