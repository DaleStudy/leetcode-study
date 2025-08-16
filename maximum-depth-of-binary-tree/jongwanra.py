"""
[Problem]
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Return maximum depth of binary tree
0 < the number of nodes < 10,000

[Brainstorming]
DFS를 이용해서 구해보자.
이진 트리에서 전체 탐색을 DFS로 진행했을 떄 시간 복잡도는 O(N)으로 판단된다.

[Complexity]
N is the number of nodes
Time: O(N)
Space: O(N)
  -> node의 개수 만큼 call stack이 쌓임
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(depth, node:Optional[TreeNode])->None:
            nonlocal answer
            if not node.left and not node.right:
                answer = max(answer, depth)
                return

            if node.left:
                dfs(depth + 1, node.left)
            if node.right:
                dfs(depth + 1, node.right)

        if not root:
            return answer
        dfs(1, root)
        return answer


class AnotherSolution:
    """
    ref: leetcode

    [Complexity]
    Time: O(N)
    Space: O(N)
    """
    def maxDepth(self, root:Optional[TreeNode])-> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


