"""
시간복잡도 : O(V + E)
공간복잡도 : O(V)

1. made 딕셔너리를 초기화한다.
2. copy_node 함수를 정의한다.
3. copy_node 함수는 target 노드를 복사한 후 반환한다.
4. 이미 복사한 노드는 made에서 재사용한다.
5. 복사한 노드의 이웃들 또한 copy_node를 이용해 재귀적으로 복사한다.
6. 최종적으로 복제된 그래프의 시작 노드를 반환한다.
"""
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        made = dict()

        def copy_node(target: Node) -> Node:
            if not target:
                return None

            copied = Node(target.val)
            made[target.val] = copied

            for nei in target.neighbors:
                if nei.val in made:
                    copied.neighbors.append(made[nei.val])
                else:
                    copied.neighbors.append(copy_node(nei))

            return copied

        return copy_node(node)
