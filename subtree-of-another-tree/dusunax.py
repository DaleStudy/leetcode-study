'''
# 572. Subtree of Another Tree

## 1. Recursive
use a recursive function to check if the two trees are identical.
- if they are identical, return True.
- if they are not identical, recursively check the left subtree and right subtree.

### base case
- isSubtree
  - if the current tree is None, return False.
  - if the subRoot is None, return True. (empty tree is a subtree of any tree)
- isIdentical
  - if both trees are None, return True. (they are identical)
  - if one of the trees is None, return False.
  - if the values of the current nodes are different, return False.
  - left subtree and right subtree's results are must be True.

## 2. Snapshot
> reference: https://www.algodale.com/problems/subtree-of-another-tree/

use a snapshot string of the preorder traversal to check if the subRoot is a subtree of the current tree.
- if the subRoot is a subtree of the current tree, return True.
- if the subRoot is not a subtree of the current tree, return False.
'''
class Solution:
    '''
    1. Recursive
    TC: O(n * m), m is the number of nodes in the subRoot.
    SC: O(n) (recursive stack space)
    '''
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        if self.isIdentical(root, subRoot): 
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isIdentical(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
            
        return s.val == t.val and self.isIdentical(s.left, t.left) and self.isIdentical(s.right, t.right)

    '''
    2. Snapshot
    TC: O(n + m), n is the number of nodes in the root, m is the number of nodes in the subRoot.
    SC: O(n + m) (recursive stack space)
    '''
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def preorder(node):
            if not node:
                return '#'
            return f'({node.val},{preorder(node.left)},{preorder(node.right)})'

        return preorder(subRoot) in preorder(root)
