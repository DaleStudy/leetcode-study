import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        주어진 이진 트리의 최대 깊이(루프에서 리프까지의 가장 긴 경로의 노드 수)를 구하는 문제
        BFS로 큐를 사용해 최대 깊이를 구함.
        Time complexity: O(n), n개의 노드를 한 번씩 방문.
        Space complexity: O(w), w는 트리의 최대 너비 (n/2).
        """
        if root is None:
            return 0
        
        depth = 0

        queue = collections.deque([root])

        while queue:
            depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return depth
