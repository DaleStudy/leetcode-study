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
            # 자식 값이 음수일경우 0으로 처리 
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # "지금까지 발견한 경로 중 최고의 합"을 res[0]에 저장
            # Job 1: 나를 꺾임점(Anchor)으로 하는 '아치형' 경로 계산
            res[0] = max(res[0], root.val + leftMax + rightMax)
            # Job 2: 부모에게 올릴 '직선' 경로 리턴
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
