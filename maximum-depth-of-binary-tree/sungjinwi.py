"""
    풀이:
        재귀함수의 탈출조건은 root가 존재하지 않을 때, return 0
        그 외에는 left, right에 재귀함수를 호출하여 더 높은 값 + 1을 return 한다
        가장 깊은 깊이의 maxDepth가 0을 return 하고 밑에서부터 + 1 씩 쌓여서 총 깊이를 return 할 수 있다
    
    노드의 개수: N

    SC : O(N)

        모든 노드에 대해 순회

    TC : O(N)

        모든 노드에 대한 재귀콜스택

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
