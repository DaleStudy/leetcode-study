class Solution:
    def levelOrder(self, root):
        result = []
        def dfs(node, level):
            if not node:
                return
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return result
