# 7기 풀이
# 시간 복잡도: O(n)
# - 트리 전체를 탐색이므로 전체 노드 개수(n) 만큼 시간 소요
# 공간 복잡도: O(h)
# - 트리의 높이(h)만큼 재귀 스택 쌓임
# - 최악의 경우(편향 트리) O(n), 평균적으로 O(log n)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val  # 결과 변수를 클래스 멤버 변수로 지정

        # 후위 탐색을 이용해서 문제를 풀면 된다
        def postorder(node):
            if not node:  # 노드가 None인 경우는 0을 리턴해준다
                return 0

            # 자식 노드들 각각의 최대합을 먼저 계산한다.
            # 자식들의 최대합이 음수인 경우는 현재 노드의 최대합 계산에 방해가 되므로
            # 0과 비교하여 더 큰 값을 저장하도록 한다
            left_total = max(postorder(node.left), 0)
            right_total = max(postorder(node.right), 0)

            # 지금까지의 최대합(self.res)와 자식 노드 및 현재 노드 val의 합을 비교하여
            # 더 큰 값을 지금까지의 최대합으로 업데이트 한다.
            # - 현재 노드가 root인 subtree의 값이 최대일 수 있기 때문에
            self.res = max(
                self.res,
                left_total + right_total + node.val
            )

            # 위로 올릴 때는 왼쪽 노드와 오른쪽 노드 최대합 중에
            # 더 큰 값을 현재 노드 value와 더해서 올려준다.
            return max(left_total, right_total) + node.val

        postorder(root)
        return self.res
