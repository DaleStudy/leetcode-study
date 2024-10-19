"""TC: O(n), SC: O(h)

h는 이진 트리의 높이. 
n이 전체 노드 개수라고 할때
- 최악의 경우 한 쪽 자식 노드만 채워짐. 이 경우 h = n.
- 최선의 경우 완전 이진 트리. h = log(n).

아이디어:
양쪽 자식 노드에 접근해서 재귀적으로 invert를 진행하고, 두 자식 노드를 바꾼다.

SC:
- 호출 스택 깊이는 트리의 깊이까지 깊어질 수 있다. 즉, O(h).

TC:
- 모든 노드에 접근. O(n).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node: Optional[TreeNode]) -> None:
            if node is not None:
                node.left, node.right = invert(node.right), invert(node.left)
            return node

        return invert(root)
