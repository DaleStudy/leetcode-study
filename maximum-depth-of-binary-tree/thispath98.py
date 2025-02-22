class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Intuition:
            왼쪽 자식과 오른쪽 자식에 대해 depth를 증가시키며 재귀하고,
            둘 중 큰 값을 반환한다.

        Time Complexity:
            O(N):
                모든 노드에 대해 재귀적으로 호출하므로 O(N)이다.

        Space Complexity:
            O(h):
                트리의 높이 h만큼 재귀 함수를 호출하므로,
                공간 복잡도는 O(h)이다.
        """

        def get_depth(node, depth):
            if not node:
                return depth

            left = get_depth(node.left, depth + 1)
            right = get_depth(node.right, depth + 1)
            return max(left, right)

        answer = get_depth(root, 0)
        return answer
