"""
 * Time Complexity: O(n)
 * Space Complexity: O(n)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        nums = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False
        return True
