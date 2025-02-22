"""
Solution: BFS 
Time: O(n)
Space: O(n)
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        maxLevel = 0
        while q:
            maxLevel += 1
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return maxLevel
