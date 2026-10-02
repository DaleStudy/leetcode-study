# TC: O(N)
# SC: O(N)
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def get_size(node):
            if not node:
                return 0
            return 1 + get_size(node.left) + get_size(node.right)

        target_size = get_size(subRoot)
        is_match = False

        def check_tree(node):
            nonlocal is_match

            if not node or is_match:
                return 0

            left_size = check_tree(node.left)
            right_size = check_tree(node.right)

            current_size = 1 + left_size + right_size

            if current_size == target_size:
                if isSameTree(node, subRoot):
                    is_match = True

            return current_size

        check_tree(root)

        return is_match

