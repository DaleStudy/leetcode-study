"""
# Approach
매 노드마다 같은 Tree인지 비교합니다.

# Complexity
- Time complexity: 양 트리의 노드를 하나씩 다 비교해야 하므로 최악의 경우 O(N*M)
- Space complexity: root 트리 높이가 H라고 할 때 O(H)만큼 재귀 스택이 쌓임
"""


class Solution:
    def isSameTree(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
