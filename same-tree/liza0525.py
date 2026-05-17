# 7기 풀이
# 시간 복잡도: O(n)
# - 두 트리의 노드 개수가 동일할 때 모든 노드를 탐색하므로 O(n)
# - 다를 경우 early return으로 그보다 적게 탐색
# 공간 복잡도: O(n)
# - stack에는 최대 트리의 너비(width)만큼 pair가 쌓임
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]  # p와 q를 tuple의 형태로 stack에 저장

        while stack:  # stack의 요소가 다 없어질 때까지 트리 탐색
            p_node, q_node = stack.pop()  # node 꺼내기

            if not p_node and not q_node:
                # 둘 다 없는 경우(null인 경우)는 leaf node로부터 온 것이기 때문에
                # 더이상 탐색을 안해도 됨 
                continue
            elif (
                not p_node and q_node
                or p_node and not q_node
            ):
                # 둘 중 하나만 null인 경우에는 tree가 같지 않으므로
                # False로 early return
                return False
            elif p_node.val != q_node.val:
                # 둘 다 있는데 값이 같지 않은 경우도
                # False로 early return
                return False

            # 두 트리의 왼쪽 쌍과 오른쪽 쌍을 각각 stack에 저장
            stack.append((p_node.left, q_node.left))
            stack.append((p_node.right, q_node.right))

        # 모든 loop를 다 돌았다면 두 트리가 같다는 의미로
        # True로 return
        return True
