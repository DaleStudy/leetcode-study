"""
시간복잡도: O(n)
공간복잡도: O(n)

- inorder 배열의 값과 인덱스를 딕셔너리로 저장하여 검색을 빠르게 함
- preorder 배열을 순서대로 순회하며 각 노드의 값을 선택함 (루트부터 하위 트리 순)
- 선택된 값을 기준으로 inorder에서 왼쪽 구간(왼쪽 서브트리의 노드 개수), 오른쪽 구간을 계산
- preorder, inorder 구간의 인덱스를 재귀적으로 갱신하여 왼쪽, 오른쪽 서브트리를 구성
- 전체 트리를 재귀적으로 구성하며 그 결과를 반환
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pos = {k: v for v, k in enumerate(inorder)}

        def build(
            pre: Tuple[int, int], ino: Tuple[int, int]
        ) -> Optional[TreeNode]:
            if pre[0] > pre[1]:
                return None

            root = TreeNode(preorder[pre[0]])
            center = pos[preorder[pre[0]]]

            left_count = center - ino[0]

            root.left = build(
                (pre[0] + 1, pre[0] + left_count),
                (ino[0], ino[0] + left_count - 1),
            )
            root.right = build(
                (pre[0] + left_count + 1, pre[1]),
                (ino[0] + left_count + 1, ino[1]),
            )

            return root

        return build((0, len(preorder) - 1), (0, len(inorder) - 1))
