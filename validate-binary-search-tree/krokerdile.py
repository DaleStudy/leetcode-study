class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            
            # 현재 노드의 값이 범위를 벗어나면 False
            if not (low < node.val < high):
                return False

            # 왼쪽 서브트리는 최대값을 현재 노드 값으로 제한
            # 오른쪽 서브트리는 최소값을 현재 노드 값으로 제한
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float('-inf'), float('inf'))
