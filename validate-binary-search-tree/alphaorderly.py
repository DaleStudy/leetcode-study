# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode], lower: Optional[int] = -float('inf'), upper: Optional[int] = float('inf')) -> bool:
#         if not root:
#             return True

#         if root.val <= lower or root.val >= upper:
#             return False

#         return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        O(N)
        """
        s = [(root, -float("inf"), float(inf))]

        while s:
            node, lower, upper = s.pop()

            if node.val <= lower or node.val >= upper:
                return False

            if node.left:
                s.append((node.left, lower, node.val))

            if node.right:
                s.append((node.right, node.val, upper))

        return True
