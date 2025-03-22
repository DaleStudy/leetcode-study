'''
시간 복잡도: O(n)
- n은 트리의 노드 수

공간 복잡도: O(h)
- h는 트리의 높이
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            # 현재 노드 값이 허용 범위를 벗어나면 False
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # 왼쪽 서브트리는 현재 값보다 작아야 하고, 오른쪽 서브트리는 현재 값보다 커야 함
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
        
        # 초기 범위는 전체 정수 범위로 설정
        return validate(root, float('-inf'), float('inf'))
