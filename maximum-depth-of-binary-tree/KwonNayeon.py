"""
Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100

Time Complexity: O(N)
- N은 트리의 노드 수
- 모든 노드를 한 번씩 방문하기 때문

Space Complexity: O(H)
- H는 트리의 높이
- 재귀 호출로 인한 호출 스택의 최대 깊이가 트리의 높이와 같음

풀이방법:
1. Base case: root가 None인 경우 0을 반환
2. 재귀를 활용하여 왼쪽과 오른쪽 서브트리 깊이를 각각 계산
3. 두 서브트리의 깊이 중 최대값에 1을 더해서 반환 (현재 노드의 깊이를 포함)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: 재귀
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
    
# Solution 2: 반복문
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [(root, 1)]
        max_depth = 0

        while stack:
            current, depth = stack.pop()
            
            max_depth = max(max_depth, depth)

            if current.left:
                stack.append((current.left, depth + 1))
            if current.right:
                stack.append((current.right, depth + 1))

        return max_depth
