"""
Solution:
    1) preOrder Traversal
    2) k 번쨰 요소 return

Time: O(n)
Space: O(n)

"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)

        return arr[k - 1]
