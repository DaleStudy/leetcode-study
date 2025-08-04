class Solution:
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t or s.val != t.val:
            return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
