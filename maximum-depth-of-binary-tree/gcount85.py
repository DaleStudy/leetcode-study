"""
# Intuition
1) BFS + 큐
2) DFS + 재귀
1번으로 풀었다가 2번이 코드가 더 간결해서 바꿨습니다. 

# Complexity
- Time complexity: 모든 노드를 다 봐야 하므로 O(N)

- Space complexity: 재귀 깊이만큼 O(H)
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            
        