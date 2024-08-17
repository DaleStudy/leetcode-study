# 시간복잡도: O(N)
# 공간복잡도: O(1)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = 0
        self.count = 0

        def dfs(node):
            if node is None:
                return

            dfs(node.left)

            self.count += 1

            if self.count == k:
                self.result = node.val
                return

            dfs(node.right)

        dfs(root)

        return self.result
