"""
Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

Time Complexity: O(n)
- 각 노드를 한 번씩만 방문함

Space Complexity: O(n)
- 결과 리스트는 모든 노드의 값을 저장함

풀이방법:
1. 루트가 없으면 빈 리스트 반환
2. 큐에 루트 넣기
3. while 큐가 빌 때까지:
  - 현재 레벨의 노드 개수 저장
  - 그 개수만큼 노드를 꺼냄
    - 노드의 값 저장
    - 자식이 있으면 큐에 추가
  - 결과에 현재 레벨을 추가
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)

        return result

