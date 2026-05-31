# https://leetcode.com/problems/maximum-depth-of-binary-tree

class Solution:
    def maxDepth(self, root):
        # base case:
        # 현재 노드가 없으면 (빈 트리 또는 leaf의 자식)
        # 깊이는 0
        if not root:
            return 0
        
        # 왼쪽 서브트리의 최대 깊이를 재귀적으로 계산
        left_depth = self.maxDepth(root.left)
        
        # 오른쪽 서브트리의 최대 깊이를 재귀적으로 계산
        right_depth = self.maxDepth(root.right)
        
        # 현재 노드를 포함해야 하므로 +1
        # 왼쪽과 오른쪽 중 더 깊은 쪽을 선택
