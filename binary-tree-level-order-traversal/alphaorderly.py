# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
시간복잡도: O(n)
  - n: 트리의 모든 노드 개수 (각 노드를 한 번씩 방문)
공간복잡도: O(n)
  - n: 최악의 경우 큐(queue)에 저장되는 노드 수(가장 마지막 레벨의 노드 수와 동일)

BFS(너비 우선 탐색)을 활용하여 트리를 레벨별로 순회하며,
각 레벨마다 노드의 값을 리스트로 모아 결과 리스트에 추가합니다.
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        ans = []

        while queue:
            temp = []
            Q = len(queue)
            for _ in range(Q):
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)

        return ans
