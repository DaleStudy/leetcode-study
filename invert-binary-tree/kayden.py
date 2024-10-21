class Solution:
    # 시간복잡도: O(N)
    # 공간복잡도: O(1)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if not node:
                return

            r = invert(node.left)
            l = invert(node.right)

            node.right = r
            node.left = l

            return node

        invert(root)

        return root
