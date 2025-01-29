"""
Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

Shallow Copy (얕은 복사):
- 노드 자체는 새로운 메모리에 복사
- 하지만 neighbors는 원본 노드의 neighbors를 그대로 참조
예시) 원본 Node1이 Node2를 neighbor로 가질 때
   복사한 CopyNode1은 새로운 노드지만
   CopyNode1의 neighbor는 원본의 Node2를 그대로 가리킴

Deep Copy (깊은 복사):
- 노드는 새로운 메모리에 복사
- neighbors도 모두 새로운 노드로 복사해서 연결
예시) 원본 Node1이 Node2를 neighbor로 가질 때
   CopyNode1도 새로운 노드이고
   CopyNode1의 neighbor도 새로 만든 CopyNode2를 가리킴

Time Complexity: O(N + E)
- N: 노드의 개수
- E: 엣지의 개수
- 모든 노드와 엣지를 한 번씩 방문

Space Complexity: O(N)
- N: 노드의 개수
- dictionary와 재귀 호출 스택 공간

# Definition for a Node.
class Node:
   def __init__(self, val = 0, neighbors = None):
       self.val = val
       self.neighbors = neighbors if neighbors is not None else []

참고 사항:
- 혼자 풀기 어려워서, 문제와 답을 이해하는 것에 집중했습니다!
"""
class Solution:
   def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
       if not node:
           return None
           
       dict = {}
       
       def dfs(node):
           if node.val in dict:  # 이미 복사한 노드라면
               return dict[node.val]  # 해당 복사본 반환
           
           # 새로운 노드 생성
           copy = Node(node.val)
           dict[node.val] = copy  # dictionary에 기록
           
           # 각 neighbor에 대해서도 같은 과정 수행
           for neighbor in node.neighbors:
               copy.neighbors.append(dfs(neighbor))
               
           return copy
       
       return dfs(node)

