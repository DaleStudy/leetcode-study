class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx_map = {
            val: idx
            for idx, val in enumerate(inorder)
        }

        def dfs(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            node = TreeNode()
            node.val = preorder[pre_start]

            in_idx = inorder_idx_map[node.val]
            left_size = in_idx - in_start

            node.left = dfs(
                pre_start + 1, pre_start + left_size,
                in_start, in_idx - 1,
            )
            node.right = dfs(
                pre_start + left_size + 1, pre_end,
                in_idx + 1, in_end,
            )

            return node

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
