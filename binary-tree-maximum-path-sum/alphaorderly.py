# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
시간복잡도: O(n)
공간복잡도: O(n)
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def calc(node: Optional[TreeNode]):
            if not node:
                # (한쪽 서브트리에서 root를 향해 올라오는 경로의 최대합, 
                #  해당 서브트리 내 임의 경로의 최대 합)
                return (-float("inf"), -float("inf"))

            # 왼쪽 서브트리 결과
            # left: 왼쪽 자식으로부터 root를 향해 이어질 수 있는 단일 경로의 최대 합
            # left_root: 왼쪽 서브트리 전체에서 얻을 수 있는 임의 경로의 최대 합
            left, left_root = calc(node.left)

            # 오른쪽 서브트리 결과
            # right: 오른쪽 자식으로부터 root를 향해 이어질 수 있는 단일 경로의 최대 합
            # right_root: 오른쪽 서브트리 전체에서 얻을 수 있는 임의 경로의 최대 합
            right, right_root = calc(node.right)

            # 한쪽(왼쪽/오른쪽) 또는 아무쪽도 안타거나(0) 현재노드로 연결 가능, 단일 경로 최대 합
            current = max(left, right, 0) + node.val
            # 현재 노드를 루트로 하는 서브트리에서 가능한 모든 경로 중 최대 합 (각 자식 0 미만이면 안탐)
            current_root = max(max(left, 0) + max(right, 0) + node.val, left_root, right_root)

            return (current, current_root)

        _, ans = calc(root)

        return ans
