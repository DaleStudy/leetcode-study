"""
Solution: val 이 같고, left, right 이 같으면 된다.
Time: O(n)
Space: O(n)
"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if q and p and q.val != p.val:
            return False
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
