from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(
        self,
        root1: Optional[TreeNode],
        root2: Optional[TreeNode]
    ) -> bool:
        leaf1 = []
        leaf2 = []
   
        def getLeaves(node, leaves):
            if node is None:
                return
            if node.left is None and node.right is None:
                leaves.append(node.val)
                return
            getLeaves(node.left, leaves)
            getLeaves(node.right, leaves)
            
        getLeaves(root1, leaf1)
        getLeaves(root2, leaf2)
        return leaf1 == leaf2


# Example trees

# root1 = [1,2,3]
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

# root2 = [1,3,2]
root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.right = TreeNode(2)


solution = Solution()
print(solution.leafSimilar(root1, root2))

# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true