# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # BFS(큐 사용)
        # 시간복잡도 O(n), 공간복잡도 O(n)

        if not root:
            return []
        
        # 큐에 root노드 추가(초기화)
        q = deque([root])
        answer = []

        # 큐가 빌 때까지 탐색(모든 노드 탐색)
        while q:
            level = []  # 현재 레벨의 노드 저장할 리스트

            for _ in range(len(q)):     # 현재 레벨에 있는 노드 수만큼 반복
                node = q.popleft()      # 큐에서 노드 꺼내서
                level.append(node.val)  # level에 저장

                # 자식 노드들이 있다면 큐에 추가
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # 현재 레벨 answer에 추가
            answer.append(level)

        return answer
