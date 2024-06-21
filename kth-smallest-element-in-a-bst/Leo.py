class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def helper(node):
            if not node: return
            helper(node.left)

            if len(ans) == k:
                return

            ans.append(node.val)
            helper(node.right)

        helper(root)
        return ans[-1]

        ## TC: O(n), SC: O(h+n) where h == heights(tree) and n == element(tree)
