# 7기 풀이
# 시간 복잡도: O(n)
# - balanced tree라면 O(log n)이 되지만, 편향 트리가 worst case이므로
# - 이때는 모든 노드 탐색, 노드 개수(n)에 따라 시간 복잡도가 결정된다.
# - balanced tree의 경우: 매 노드 탐색 때마다 한 쪽 서브 트리를 선택해 탐색하므로 노드 개수(n)의 log 값만큼의 시간 소요
# 공간 복잡도: O(h)
# - tree의 높이인 h만큼의 재귀 스택이 쌓임
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node1 = p if p.val < q.val else q  # node1은 val이 작은 노드를 가르키게 설정
        node2 = q if p.val < q.val else p  # node2은 val이 큰 노드를 가르키게 설정

        def find_lca(node):
            # BST 특징에 의해
            # 자기 자신 값은 왼쪽 서브트리 노드의 값들보다 무조건 크고
            # 오른쪽 서브트리 노드들의 값보다 무조건 작다.
            # 따라서 node1.val <= node.val <= node2.val이면
            # p와 q가 현재 노드를 기준으로 양쪽에 갈라지는 순간으로 판단,
            # 그 노드가 LCA가 된다.
            if node1.val <= node.val <= node2.val:
                # 사이에 들어온 경우는 node 그 자체를 return
                # 등호도 같이 써준다.
                return node
            elif node.val > node1.val and node.val > node2.val:
                # node의 값이 node1의 값과 node2의 값보다 큰 경우,
                # LCA는 현재 노드의 left subtree에 존재한다는 의미이므로
                # 다음 탐색은 왼쪽 자식 노드 쪽으로 재귀 탐색
                return find_lca(node.left)
            elif node.val < node1.val and node.val < node2.val:
                # node의 값이 node1의 값과 node2의 값보다 작은 경우,
                # LCA는 현재 노드의 right subtree에 존재한다는 의미이므로
                # 다음 탐색은 오른쪽 자식 노드 쪽으로 재귀 탐색
                return find_lca(node.right)
            
            # 세 케이스가 exhaustive하므로 else 없음

        return find_lca(root)
