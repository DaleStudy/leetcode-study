# 7기 풀이
# 풀이 1, 2 모두 중위 순회를 하면 BST를 오름차순으로 순회할 수 있다는 특징을 이용해 풀이
class Solution:
    # 풀이 1
    # 시간 복잡도: O(n)
    # - 최악의 경우에는 모든 노드를 탐색하는 경우이므로, 노드의 개수(n)만큼의 시간 소요
    # 공간 복잡도: O(h)
    # - 재귀 스택에 트리의 깊이(h) 만큼 사용됨
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1  # 결과를 저장할 변수

        def inorder(node):
            # k와 res는 inorder 함수 외부의 변수들이므로,
            # nonlocal 선언하여 접근할 수 있게 변경 
            nonlocal k
            nonlocal res

            if not node:
                # 노드가 None인 경우는 재귀 탐색을 끝내고 return
                return

            inorder(node.left)  # 왼쪽 자식 노드를 재귀적으로 먼저 탐색
            k -= 1  # 현재 노드 탐색에서 k를 하나 줄임
            if k == 0:  # k가 0이 되는 순간이 전체 노드 중에 k번째 값이 됨
                res = node.val  # res에 node의 값을 할당
                return  # 더이상 탐색할 필요가 없으므로 return
            inorder(node.right)  # 오른쪽 자식 노드를 재귀적으로 나중에 탐색

        inorder(root)
        return res

    # 풀이 2
    # 시간 복잡도: O(n)
    # - 모든 노드를 탐색하기 때문에 노드의 개수(n)만큼의 시간 소요
    # 공간 복잡도: O(n)
    # - 모든 노드의 값을 res_list에 저장하기 때문에 노드의 개수(n)만큼의 공간 차지
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res_list = []

        def inorder(node):
            if not node:
                # 노드가 없을 땐 return
                return

            inorder(node.left)  # 왼쪽 자식 노드를 재귀적으로 먼저 탐색
            res_list.append(node.val)  # 현재 노드를 res_list에 삽입
            inorder(node.right)  # 오른쪽 자식 노드를 재귀적으로 나중에 탐색


        inorder(root)  # 중위 탐색 시작
        return res_list[k - 1]  # 탐색한 결과 중 k번째 요소 return
