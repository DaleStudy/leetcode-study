# 시간 복잡도: O(n)
# - 트리의 모든 노드를 한 번씩 방문하면서 깊이 계산
# - 각 노드는 정확히 한 번만 처리되므로 전체 노드 수 n에 비례

# 공간 복잡도: O(h)
# - 재귀 호출 스택의 최대 깊이는 트리의 높이(h)만큼 쌓임
# - 균형 트리면 O(log n), 일자로 치우친 트리(skewed tree)면 O(n)까지 갈 수 있다.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 현재 노드(cur_node)를 기준으로 왼쪽/오른쪽 서브트리의 최대 깊이를 구하고
    # 그 중 큰 값을 반환하는 재귀 함수을 사용
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth는 지금까지 내려온 깊이를 의미
        def find_max_depth(cur_node, depth):
            # 더 내려갈 노드가 없다면(leaf의 자식) 지금까지의 depth가 해당 경로의 깊이
            if not cur_node:
                return depth

            # 왼쪽으로 한 단계 내려가면서 깊이를 증가시켜 탐색
            left_depth = find_max_depth(cur_node.left, depth + 1)
            # 오른쪽도 동일하게 탐색
            right_depth = find_max_depth(cur_node.right, depth + 1)

            # 왼쪽/오른쪽 중 더 깊은 쪽이 이 노드 기준 최대 깊이
            return max(left_depth, right_depth)

        # 루트에서 시작하며 깊이는 0부터 시작
        max_depth = find_max_depth(root, 0)

        return max_depth
