"""TC: O(n + e), SC: -

노드 개수 n개, 엣지 개수 e개

아이디어:
문제 설명부터가 deepcopy를 하라는 것이니 내장함수를 써서 deepcopy를 해주자.

SC:
- 내장함수가 필요한 공간들을 따로 잘 관리해주지 않을까? 아마 변수를 읽고 그대로 리턴값으로 바꿔줄듯.
- 그렇다면 추가적으로 관리하는 공간은 필요 없다.

TC:
- deepcopy는 필요한 정보를 그대로 다 deepcopy 뜰 뿐이다. 아마 node 개수 + edge 개수에 비례해서 시간이
  걸릴것 같다. O(n + e).
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

import copy
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        return copy.deepcopy(node)


"""TC: O(e), SC: O(e)

노드 개수 n개, 엣지 개수 e개

아이디어:
dfs 돌면서 노드들을 메모해두자. neighbors에 특정 노드를 추가해야 할때 메모에 있으면 바로 가져다
쓰고, 없으면 새로 만들어서 메모에 노드를 추가한다.

SC:
- 노드 총 n개가 memo에 올라간다. O(n).
- 각 노드마다 neighbor가 있다. 각 edge마다 neighbor 리스트들의 총 아이템 개수에 2개씩 기여한다. O(e).
- 더하면 O(n + e). 즉, 둘 중 더 큰 값이 공간복잡도를 지배한다.
  ...고 생각하는 것이 일차적인 분석인데, 여기서 더 나아갈 수 있다.
- 주어진 조건에 따르면 우리에게 주어진 그래프는 connected graph다. 즉, 엣지 개수가 n-1개 이상이다.
- 즉, O(n) < O(e)가 무조건 성립하므로, O(e) < O(n + e) < O(e + e) = O(e). 즉, O(e).

TC:
- SC와 비슷한 방식으로 분석 가능. O(e).
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return node

        memo = {}

        def dfs(node):
            if node not in memo:
                new_node = Node(node.val, [])
                memo[node] = new_node
                new_node.neighbors = [dfs(i) for i in node.neighbors]
            return memo[node]

        return dfs(node)
