from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        has_subroot_in_left = self.isSubtree(root.left, subRoot)
        has_subroot_in_right = self.isSubtree(root.right, subRoot)

        return has_subroot_in_left or has_subroot_in_right

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        - Idea: 두 트리를 다음과 같이 노드 단위로 비교한다.
            1. 두 노드가 모두 None이라면 현재 두 트리는 동일
            2. 두 노드가 None이 아니고 값이 같다면, 왼쪽과 오른쪽 자식 노드를 재귀적으로 비교
            3. 두 노드가 다르거나 한쪽만 None이면 두 트리는 상이
        - Time Complexity: O(m). m은 더 작은 트리의 노드 수
            각 노드를 한번씩 방문하므로 O(m) 시간이 걸린다.
        - Space Complexity: O(h). h는 더 작은 트리의 높이
            재귀 호출 스택에 최대 h만큼의 공간이 사용된다.
        """

        if not p and not q:
            return True

        if p and q and p.val == q.val:
            is_left_equal = self.isSameTree(p.left, q.left)
            is_right_equal = self.isSameTree(p.right, q.right)

            return is_left_equal and is_right_equal

        return False
