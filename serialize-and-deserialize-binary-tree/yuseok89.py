# TC: O(N)
# SC: O(N)
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

        arr = []
        q = deque()
        q.append(root)

        while q:

            cur = q.popleft()

            if cur:
                arr.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
            else:
                arr.append('n')

        return ','.join(arr)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        values = data.split(',')
        n = len(values)

        if values[0] == 'n':
            return None

        root = TreeNode(int(values[0]))
        q = deque()
        q.append(root)
        idx = 1

        while idx < n:
            par = q.popleft()

            if values[idx] != 'n':
                par.left = TreeNode(int(values[idx]))
                q.append(par.left)
            idx += 1

            if idx < n and values[idx] != 'n':
                par.right = TreeNode(int(values[idx]))
                q.append(par.right)
            idx += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

