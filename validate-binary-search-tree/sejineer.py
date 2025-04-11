"""
시간 복잡도: O(N)
공간 복잡도: O(N)
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        num_list = []

        def dfs(node: TreeNode):
            if not node:
                return
            
            dfs(node.left)
            num_list.append(node.val)
            dfs(node.right)
        
        dfs(root)

        mem = num_list[0]
        for i in range(1, len(num_list)):
            if mem >= num_list[i]:
                return False
            mem = num_list[i]
        return True
