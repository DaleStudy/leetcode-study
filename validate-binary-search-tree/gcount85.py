"""
# https://leetcode.com/problems/validate-binary-search-tree/description/
# Intuition
BST를 중위 순회하면 오름차순으로 값이 정렬된다는 점에 착안했습니다.

# Complexity
- Time complexity: 노드의 개수를 N이라고 할 때, O(N)

- Space complexity: 재귀로 트리를 순회하면서 호출 스택이 쌓이는데
트리의 높이를 H라고 할 때, 호출 스택은 H 만큼 쌓입니다. => 공간 복잡도 O(H)
"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [None]

        def inorder(node):
            if not node:
                return True

            if not inorder(node.left):
                return False

            if prev[0] is not None and prev[0] >= node.val:
                return False
            prev[0] = node.val

            return inorder(node.right)

        return inorder(root)
