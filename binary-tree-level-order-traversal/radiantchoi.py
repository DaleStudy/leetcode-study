from collections import deque, defaultdict
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 앞으로의 코드는 root가 있다는 것을 전제로 수행
        # 또한 root가 None이라면 기록해서 돌려 줄 값도 없기 때문에 early return
        if not root:
            return []

        # depth별 노드를 기록할 defaultdict
        nodes = defaultdict(list)
        # bfs 탐색에 사용될 queue
        queue = deque()

        # root는 존재함이 보장되므로, 반복문의 시동을 위해 root node를 queue에 추가
        # 이 때 깊이 정보도 함께 묶어서 tuple로 추가
        queue.append((root, 0))

        while queue:
            current = queue.popleft()

            # 현재 노드의 값 기록
            nodes[current[1]].append(current[0].val)

            # 현재 노드의 왼쪽 자식 노드가 존재한다면, 해당 노드와 깊이 정보를 함께 queue에 추가
            if current[0].left:
                queue.append((current[0].left, current[1] + 1))
                
            # 현재 노드의 오른쪽 자식 노드가 존재한다면, 해당 노드와 깊이 정보를 함께 queue에 추가
            if current[0].right:
                queue.append((current[0].right, current[1] + 1))

        # 깊이 순서대로 dict에 추가되었으므로, values()를 사용하여 리스트로 변환하여 반환
        return list(nodes.values())
