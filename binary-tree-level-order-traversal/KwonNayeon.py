"""
Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

Time Complexity: O(n)
- 각 노드를 한 번씩만 방문함

Space Complexity: O(n)
- 결과 리스트는 모든 노드의 값을 저장함

풀이방법:
1. queue와 BFS를 활용하여 레벨 순서로 노드를 순회
2. 각 레벨의 노드들을 별도의 리스트로 모아서 결과에 추가
3. 각 노드를 처리할 때 그 노드의 자식들을 큐에 추가하여 다음 레벨로 넘어감
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
