# H is the height of the BST, and K is the target rank.
# TC: O(H + K) - in-order traversal stops after visiting K elements
# SC: O(H) - stack memory for in-order traversal recursion/loop

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def kthSmallest(self, root, k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right

        return -1
