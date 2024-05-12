# Time complexity : O(n*m)
# Space complexity : Space complexity: O(h) h is the height of the call stack during the recursive traversal.
class Solution:
    def isSubtree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q:
            return True

        if not p:
            return False

        if self.isSameTree(p, q):
            return True

        return self.isSubtree(p.left, q) or self.isSubtree(p.right, q)

    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True

        if not p and q:
            return False

        if p and not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
