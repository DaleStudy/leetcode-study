class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = 0
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            inorder(node.right)
        inorder(root)
        return self.result
