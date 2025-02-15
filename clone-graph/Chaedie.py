"""
한번에 풀지 못해 다시 풀어볼 예정입니다.

Solution:
    1) oldToNew 라는 dict 를 만들어 무한루프를 방지합니다.
    2) newNode = Node(node.val), newNode.neighbors.append(dfs(nei)) 를 통해 clone을 구현합니다.

정점 V, 간선 E
Time: O(V + E)
Space: O(V + E)
"""


class Solution:
    def cloneGraph(self, root: Optional["Node"]) -> Optional["Node"]:
        if not root:
            return None
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            newNode = Node(node.val)
            oldToNew[node] = newNode

            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))

            return newNode

        return dfs(root)
