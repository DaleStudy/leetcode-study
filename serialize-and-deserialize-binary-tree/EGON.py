from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """
    Runtime: 76 ms (Beats 85.72%)
    Time Complexity: O(n)
    > dfs를 통해 모든 node를 방문하므로, O(n)

    Memory: 21.40 MB (Beats 12.82%)
    Space Complexity: O(n)
    > 일반적인 경우 트리의 깊이만큼 dfs 호출 스택이 쌓이나, 최악의 경우 한쪽으로 편향되었다면 트리의 깊이가 n이 될 수 있으므로 O(n), upper bound
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                result.append("null")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        result = []
        dfs(root)
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs() -> Optional[TreeNode]:
            val = next(values)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        values = iter(data.split(','))
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
