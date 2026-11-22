"""
https://leetcode.com/problems/validate-binary-search-tree/description/

시간 복잡도 : O(n)
공간 복잡도 : O(n)
"""

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        def dfs(node, lower, upper,):
            if node is None:
                return True

            if not lower < node.val < upper:
                return False

            return (
                dfs(node.left, lower, node.val)
                and dfs(node.right, node.val, upper)
            )

        return dfs(root, float("-inf"), float("inf"))
