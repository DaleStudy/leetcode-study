# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Solution: DFS
    1) dfs 로 left, right 각각의 max 값을 구한다.
    2) maxSum 을 업데이트하고, 
    3) return value 로는 leftMax 또는 rightMax 와의 합만 리턴한다. 
    (left, right 를 둘 다 포함하는 경우와 둘 중 하나만 선택하는 경우를 나눔)

Time: O(n)
Space: O(n)

"""


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val

        def dfs(root):
            nonlocal maxSum
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            maxSum = max(maxSum, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return maxSum
