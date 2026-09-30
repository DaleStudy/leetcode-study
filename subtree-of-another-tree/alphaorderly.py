"""
시간복잡도: O(n + m)
공간복잡도: O(n + m)

- subRoot 트리를 후위 순회하여 배열로 변환
- root의 각 노드마다 후위 순회 결과 배열을 구함
- 이 배열이 subRoot의 후위 순회 배열과 일치하는지 확인
- 같으면 True 반환, 아니면 계속 탐색
"""
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def postorder(node: TreeNode):
            if not node:
                return ["*"]

            left = postorder(node.left)
            right = postorder(node.right)
            return left + right + [node.val]

        sub_pos = postorder(subRoot)

        def check(node: TreeNode):
            if not node:
                return (["*"], False)

            left, left_valid = check(node.left)
            right, right_valid = check(node.right)

            if left_valid or right_valid:
                return ([], True)

            if left + right + [node.val] == sub_pos:
                return ([], True)

            return (left + right + [node.val], False)

        return check(root)[1]
