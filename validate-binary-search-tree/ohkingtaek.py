class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        DFS로 각 노드가 low < node.val < high 조건을 만족하는지 확인한다.
        low와 high는 각각 왼쪽과 오른쪽 서브트리에서의 최대값과 최소값을 나타내며, 재귀적으로 확인한다.
        """        
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float('inf'))
