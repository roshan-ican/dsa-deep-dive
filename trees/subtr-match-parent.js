
  class TreeNode {
      constructor(val = 0, left = null, right = null) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
}
 

class Solution {
    isSubtree(root, subRoot) {
        if(!root) return false
        if(this.isMatch(root, subRoot)) {
            return true
        }
        return this.isSubtree(root.left, subRoot) || 
            this.isSubtree(root.right, subRoot)
    }

    isMatch(root, subRoot) {
        if(root === null && subRoot === null){
            return true
        }
        if(root === null || subRoot === null){
            return false
        }
        if(root.val !== subRoot.val) return false

        return this.isMatch(root.left, subRoot.left) && this.isMatch(root.right, subRoot.right)
    }

}

const root = new TreeNode(
    1,
    new TreeNode(2,
        new TreeNode(4),
        new TreeNode(5)
    ),
    new TreeNode(3)
)

const subRoot = new TreeNode(
    2,
    new TreeNode(4),
    new TreeNode(5)
)



const sol = new Solution()

console.log(sol.isSubtree(root, subRoot)) // t
console.log(sol.isSubtree(root, subRoot)) // true