from typing import Optional

# 7기 풀이
# 시간 복잡도: O(V + E)
# - 모든 노드의 수와 모든 엣지의 수만큼 탐방하므로 그만큼의 시간이 걸림(V: 노드 수, E: 엣지 수)
# 공간 복잡도: O(V)
# - memo에 모든 노드를 복사해서 추가(V: 노드의 갯수)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        memo = {}

        def copy_graph(node):
            if not node:
                # 더이상 복사할 노드가 없다면 None을 return
                return None

            if node.val in memo:
                # node의 값이 memo에 있다면 memo에 있는 값을 return
                return memo[node.val]

            # Node의 복사를 위해 새 노드 생성 및 node.val 값을 초기값으로 입력
            res_node = Node(node.val)
            memo[node.val] = res_node  # memo에 새로만든 객체를 value로 하여 저장(key는 node.val 값으로)

            # neighbors도 복사, 이 때 copy_graph를 재귀로 호출하여 모든 neighbors들을 복사하도록 한다.
            res_node.neighbors = [
                copy_graph(neighbor) for neighbor in node.neighbors
            ]

            # res_node를 return
            return res_node

        return copy_graph(node)# 다음과 같이 파이썬의 built-in 함수인 deepcopy를 사용하면 바로 문제가 풀리기도 했다.


# 정리 목적
# 다음과 같이 파이썬의 built-in 함수인 deepcopy를 사용하면 바로 문제가 풀리기도 했다.
# 실제 deepcopy 구현이 memo를 이용하며
# copier의 deepcopy를 호출하여 재귀와 비슷하게 구현했다는 것을 확인할 수 있었다
# ref: https://github.com/python/cpython/blob/main/Lib/copy.py
from copy import deepcopy


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return deepcopy(node)
