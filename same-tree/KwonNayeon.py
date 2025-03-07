"""
Constraints:
- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4

Time Complexity: O(n)
- 각 노드를 한 번씩 방문

Space Complexity: O(h)
- 재귀 호출 스택의 깊이는 트리의 높이(h)에 비례함

풀이방법:
1. DFS와 재귀를 활용하여 두 트리를 동시에 탐색
2. base case:
   - p와 q가 모두 None이면 → 같은 트리
   - 둘 중 하나만 None이거나 노드의 값이 다르면 → 다른 트리
3. 재귀로 왼쪽과 오른쪽 서브트리가 모두 같은지 확인
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

