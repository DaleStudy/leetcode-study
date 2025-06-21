class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                vals.append("None")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        vals = []
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        def dfs():
            val = next(vals)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        vals = iter(data.split(","))
        return dfs()
