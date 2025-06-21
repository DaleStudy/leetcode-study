# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preorder_ser(node):
            # base condition
            if not node:
                res.append("None")
                return

            # traversal
            res.append(str(node.val))
            preorder_ser(node.left)
            preorder_ser(node.right)

        preorder_ser(root)

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        from collections import deque

        preorder_vals = deque(data.split(","))

        def preorder_deser():
            val = preorder_vals.popleft()

            # base condition
            if val == "None":
                return None

            # traversal
            node = TreeNode(int(val))
            node.left = preorder_deser()
            node.right = preorder_deser()

            return node

        return preorder_deser()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
