from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        nodes = []
        
        q = deque([[root, 1]])

        while q:
            node, idx = q.popleft()
            if not node:
                continue
            nodes.append(str(idx)+":"+str(node.val))
            q.append([node.left, idx*2])
            q.append([node.right, idx*2+1])
        
        return '/'.join(nodes)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None

        data = data.split('/')

        node_dict = {}

        for chunk in data:
            idx, val = chunk.split(':')
            node_dict[int(idx)] = val

        def dfs(idx):
            if idx in node_dict:
                node = TreeNode(int(node_dict[idx]))
                node.left = dfs(idx*2)
                node.right = dfs(idx*2+1)
                return node
            else:
                return None

        return dfs(1)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
