class Codec:
    """
    Solution: DFS
    Time: O(n)
    Space: O(n)
    """

    def serialize(self, root):
        arr = []

        def dfs(node):
            if not node:
                arr.append("null")
                return

            arr.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(arr)

    """
    Solution: DFS
    Time: O(n)
    Space: O(n)
    """

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "null":
                self.i += 1
                return None

            node = TreeNode()
            node.val = vals[self.i]
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
