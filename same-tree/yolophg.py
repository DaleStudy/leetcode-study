# Time Complexity: O(N) - visit each node once.
# Space Complexity: O(N) in the worst case (skewed tree), O(log N) in the best case (balanced tree).

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        # if both trees are empty, they are obviously the same
        if p is None and q is None:
            return True  
        
        # if one tree is empty but the other is not, they can't be the same
        if p is None or q is None:
            return False
        
        # if values of the current nodes are different, trees are not the same
        if p.val != q.val:
            return False
        
        # recursively check both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
