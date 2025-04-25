# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#val: 노드의 값, left: 왼쪽 자식 노드, right: 오른쪽 자식 노드
#helper 함수: 재귀적으로 BST의 유효성을 검사
#lower: 현재 노드의 값이 가져야 하는 최소값
#upper: 현재 노드의 값이 가져야 하는 최대값 

class Solution:
    def isValidBST(self, root: TreeNode):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            
            # BST 조건 검사 현재 노드의 값이 허용되는 범위를 벗어나는지 확인(벗어나면 false 반환)
            if node.val <= lower or node.val >= upper:
                return False
            
            # 왼쪽 서브트리 검사 (상한을 현재 노드의 값으로 설정)
            if not helper(node.left, lower, node.val):
                return False
            
            # 오른쪽 서브트리 검사 (하한을 현재 노드의 값으로 설정)
            if not helper(node.right, node.val, upper):
                return False
            
            return True
        
        return helper(root)

        #시간 복잡도: O(n)
            #모든 노드를 한번씩 방문
        #공간 복잡도: O(n)
            #재귀 호출 스택의 깊이가 트리의 높이만큼 필요



