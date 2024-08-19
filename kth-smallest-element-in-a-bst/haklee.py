"""TC: O(n), SC: O(n)

BST의 전체 노드 개수가 n개라고 가정.

TC는 최악의 경우 BST 노드 전체를 순회해야 하므로 O(n).

노드를 순회하면서 지나온 노드 값을 따로 저장하지 않고 카운터로 처리하고 있다.
즉, traverse 함수를 재귀적으로 호출하는 부분의 콜 스택의 깊이 값만 고려하면 되는데,
root 노드부터 전부 left로 이어진 트리가 만들어질 경우 SC가 O(n)으로 최악.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global cnt
        cnt = 0

        def traverse(node: Optional[TreeNode]) -> int:
            """아이디어:
            노드의 왼쪽 자식을 먼저 순회하고,
            본인의 값을 체크하면서 cnt값을 늘리고,
            노드의 오른쪽 자식을 순회.

            순회하다가 cnt값이 k가 되면, 즉, k번째 작은 원소를 찾으면
            순회를 멈추고 찾은 값을 리턴.

            리턴된 값이 -1인 경우 순회 중 원하는 값을 찾지 못했다는 뜻이다.
            문제 조건에서 노드의 val 값이 0 이상이라고 되어있어서 -1을 선택.
            """
            global cnt
            return -1 if not node\
                else v if (v := traverse(node.left)) >= 0\
                else node.val if (cnt := cnt + 1) == k\
                else traverse(node.right)

        return traverse(root)
