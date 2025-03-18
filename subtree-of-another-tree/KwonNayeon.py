"""
Constraints:
- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4

Time Complexity: O(m * n)
- m: root의 노드 수
- n: subRoot의 노드 수

Space Complexity: O(m)
- 재귀 호출 스택의 최대 깊이 = root의 높이(?)

풀이방법:
1. Base case 처리:
  - subRoot가 없을 때 → True
  - root가 빈 트리이고, subRoot가 있을 때 → False
2. 각 노드를 비교하여 동일한 트리인지 판단하는 함수 활용:
  - isSameTree 함수: 두 트리가 동일한지 체크
  - 현재 노드부터 시작해서 같은지 확인
  - 같지 않다면 재귀를 활용하여 왼쪽/오른쪽 자식 검사
3. 재귀를 활용하여 각 노드에서 서브트리 검사:
  - 현재 노드부터 시작하는 서브트리가 subRoot와 같은지 확인
  - 아니면 왼쪽/오른쪽 서브트리에서 검사
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
