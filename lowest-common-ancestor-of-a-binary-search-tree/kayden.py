class Solution:
    # 시간복잡도: O(N)
    # 공간복잡도: O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node):
            if not node:
                return None

            left = find(node.left)
            right = find(node.right)

            if node == p or node == q:
                return node

            if left and right:
                return node

            return left or right

        return find(root)
