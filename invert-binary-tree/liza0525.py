# 7기 풀이
# 시간 복잡도: O(n)
# - 노드의 개수(n)만큼 시간 소요
# 공간 복잡도: O(h)
# - 주어진 트리의 높이(h)만큼 재귀 스택 사용
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert_binary_tree(node):
            if not node:
                return

            # 트리 탐색 시 right -> left 순서로 순회하도록 재귀 호출
            invert_binary_tree(node.right)
            invert_binary_tree(node.left)

            # node의 right와 left를 서로 바꿔준다.
            node.right, node.left = node.left, node.right

        invert_binary_tree(root)
        return root
