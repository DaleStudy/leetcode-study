"""
# Approach
노드를 방문하면서 왼쪽 자식, 오른쪽 자식을 서로 교체합니다.
이 과정을 왼쪽/오른쪽 서브트리에 재귀적으로 반복합니다.

# Complexity
- Time complexity: 모든 노드를 다 방문해야 하기 때문에 O(N)
- Space complexity: 재귀 호출 스택이 트리 높이만큼 쌓일 수 있기 때문에 O(H)
"""


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
