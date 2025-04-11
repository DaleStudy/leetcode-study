"""
Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

<Solution 1: 재귀>
Time Complexity: O(n)
- 트리의 모든 노드를 한 번씩 방문함

Space Complexity: O(h)
- 스택에는 최대 h개의 노드가 저장됨 (h는 트리의 높이)

풀이방법:
1. 각 노드가 가질 수 있는 값의 범위를 한정함
  - root 노드의 범위는 (-무한대, +무한대)로 설정
2. Base case:
  - 빈 노드의 경우 True
  - 노드 값이 범위를 벗어나면 False
3. 재귀를 활용:
  - 왼쪽 서브트리: max_val를 현재 노드 값으로 업데이트 (모두 현재 값보다 작아야 함)
  - 오른쪽 서브트리: min_val을 현재 노드 값으로 업데이트 (모두 현재 값보다 커야 함)
  - 왼쪽과 오른쪽 서브트리가 모두 조건을 만족하면 BST
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False
                
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        return validate(root, float("-inf"), float("inf"))

"""
<Solution 2: 반복문>
Time Complexity: O(n)
- 트리의 모든 노드를 한 번씩 방문함

Space Complexity: O(h)
- 스택에는 최대 h개의 노드가 저장됨 (h는 트리의 높이)

노트:
- 재귀와 동일한 순서로 노드를 방문함 (왼쪽 서브트리 → 현재 노드 → 오른쪽 서브트리)
- 트리가 매우 깊어질 경우 발생할 수 있는 스택 오버플로우를 방지할 수 있음
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        pre_val = float('-inf')
        current = root

        while current or stack:
            
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if current.val <= pre_val:
                return False

            pre_val = current.val
            current = current.right

        return True

