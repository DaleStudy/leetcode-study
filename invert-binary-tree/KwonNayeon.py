"""
Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

<Solution 1>
Time Complexity: O(n)
- 각 노드를 한 번씩 방문함

Space Complexity: O(w)
- w는 트리의 최대 너비(width)

풀이방법:
1. 큐를 사용한 BFS(너비 우선 탐색)
2. FIFO(First In First Out)로 노드를 처리함
3. 각 노드를 방문할 때마다:
   - 왼쪽과 오른쪽 자식 노드의 위치를 교환
   - 교환된 자식 노드들을 큐에 추가하여 다음 노드를 처리함

<Solution 2>
Time Complexity: O(n)
- 각 노드를 한 번씩 방문함

Space Complexity: O(h)
- h는 트리의 높이, 재귀 호출 스택의 최대 깊이

풀이방법:
1. DFS(깊이 우선 탐색)와 재귀를 활용
2. 각 노드에서:
  - 왼쪽과 오른쪽 자식 노드의 위치를 교환
  - 재귀적으로 왼쪽, 오른쪽 서브트리에 대해 같은 과정 반복
3. Base case: root가 None이면 None 반환
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# Solution 1 (BFS 활용)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

# Solution 2 (DFS와 재귀 활용)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
