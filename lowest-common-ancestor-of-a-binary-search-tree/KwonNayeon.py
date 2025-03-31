"""
Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST.

Time Complexity: O(h)
- 여기서 h는 트리의 높이

Space Complexity: O(1)
- node 변수만 사용하므로 상수공간

풀이방법:
1. LCA 노드란:
  - 두 노드 중 하나가 다른 하나의 조상인 경우, 상위에 위치한 노드가 LDA
  - 그렇지 않으면, 두 노드를 타고 위로 올라가면 처음 만나는 노드가 LDA
2. BST에서 LCA 찾기:
  - 현재 노드의 값이 p와 q보다 큰 경우 -> 왼쪽으로 이동
  - 현재 노드의 값이 p와 q보다 작은 경우 -> 오른쪽으로 이동
  - 그 외의 경우(현재 노드가 p와 q 사이에 있거나 p나 q 중 하나와 같으면) -> 현재 노드가 LCA
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root

        while node:

            if p.val < node.val and q.val < node.val:
                node = node.left

            elif p.val > node.val and q.val > node.val:
                node = node.right

            else:
                return node
