# Time complexity : O(n)
# Space complexity : O(n)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            node = stack.pop()

            # Not accessing child if node is Null
            if not node:
                continue

            node.left, node.right = node.right, node.left
            stack += [node.left, node.right]

        return root
