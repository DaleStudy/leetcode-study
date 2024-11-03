"""TC: O(n), SC: O(h)

n은 주어진 트리 p, q의 노드 개수 중 더 작은 쪽의 값.
h는 주어진 트리 p의 높이.

아이디어:
- p를 dfs로 돌면서 q도 같은 순서로 dfs를 돌린다.
- 이때 순회하다가 하나라도 다른 값이 나오면 False. 모두 같으면 True.

SC:
- p를 기준으로 dfs를 돌고 있으므로 호출 스택의 깊이가 p의 깊이보다 깊어질 수 없다. O(h).

TC:
- 최악의 경우 모든 노드 순회 후 True 리턴. O(n).
- False를 리턴할 경우 트리 순회 중 멈춘다. 이 경우 두 트리 중 더 적은 노드 개수 보다
  적은 회수 만큼 순회. 이 경우에도 O(n).
- 종합하면 O(n).
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (p is None and q is None) or (
            p is not None
            and q is not None
            and p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
