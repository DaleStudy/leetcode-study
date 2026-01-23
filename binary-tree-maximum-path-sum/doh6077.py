# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # # Initially thought I need to use BFS ( misunderstood the question)
        # if not root:
        #     return 
        # queue = deque([root])
        # result = []
        # val = 0
        # max_sum = float('-inf') 
        # while queue:
        #     currentNode = queue.popleft()
        #     result.append(currentNode.val)
        #     val += currentNode.val

        #     if currentNode.left:
        #         queue.append(currentNode.left)
        #         val += currentNode.left.val
        #     if currentNode.right:
        #         queue.append(currentNode.right)
        #         val += currentNode.right.val
        #     max_sum = max(val, max_sum)
        #     val = 0
        # return max_sum
        res = [root.val]

        def dfs(root):
            if not root:
                return 0 
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
