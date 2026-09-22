# TC: O(N)
# SC: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        ret = []

        def preOrder(root: TreeNode | None, height: int):
            if len(ret) == height:
                ret.append([])

            ret[height].append(root.val)

            if root.left:
                preOrder(root.left, height + 1)
            if root.right:
                preOrder(root.right, height + 1)

        if root:
            preOrder(root, 0)

        return ret

