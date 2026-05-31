# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        return validate(root, float('-inf'), float('inf'))


"""
================================================================================
풀이 과정
================================================================================

[1차 시도] 단순 재귀
────────────────────────────────────────────────────────────────────────────────
4. left < node < right 체크를 해줘야하고
5. 각 노드는 자신의 서브트리에서 최소값과 최대값을 가지고 있어야함
6. 현재 노드보다 왼쪽은 작은 값, 오른쪽은 큰 값
7. 재귀적으로 구현할 수 있음

        def validate(node, min_val, max_val):
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            # 재귀적으로 왼쪽, 오른쪽 서브트리 체크
            # 왼쪽 서브트리는 현재 노드 값보다 작아야하고, 오른쪽 서브트리는 현재 노드 값보다 커야함
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        return validate(root, float('-inf'), float('inf'))

8. 시간 복잡도: O(n) - 모든 노드를 한 번씩 방문
9. 공간 복잡도: O(h) - 재귀 호출 스택 (h는 트리 높이)
10. 재귀적으로 스택 오버플로우가 발생하는 것이 우려되면 iterative로 구현할 수 있음
"""
