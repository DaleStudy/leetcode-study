from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        - Idea: 너비 우선 탐색(BFS)를 이용하여 이진 트리를 단계 별로 순회한다.
        - Time Complexity: O(n). n은 트리의 노드 수.
            모든 노드를 한번씩 방문하므로 O(n) 시간이 걸린다.
        - Space Complexity: O(n). n은 트리의 노드 수.
            가장 아래 단계에 있는 노드를 저장할 때 가장 많은 메모리를 사용하고, 이는 n에 비례하기 때문에 O(n) 만큼의 메모리가 필요하다.
        """
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
