"""TC: O(n), SC: O(1)

n은 주어진 트리의 노드 개수.

아이디어:
- 트리 구조를 dict로 만들어버리자.
    - Node = None | {v: int, l: Node, r: Node}
- 이 dict를 python에 있는 json 패키지를 써서 string으로 바꾸고, string에서 불러온다.

SC:
- dict에 들어가는 정보의 크기는 노드 개수만큼 커지며, 이걸 그대로 string으로 바꾸기 때문에 
  노드 개수에 비례하여 증가. O(n).

TC:
- serialize, deserialize 과정 모두 노드 개수만큼 순회. O(n).
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import json


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def write_node(node):
            d = None
            if node:
                d = {
                    "v": node.val,
                    "l": write_node(node.left),
                    "r": write_node(node.right),
                }
            return d

        return json.dumps(write_node(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = json.loads(data)

        def read_data(d):
            if d is None:
                return None

            node = TreeNode(d["v"])
            node.left = read_data(d["l"])
            node.right = read_data(d["r"])

            return node

        return read_data(data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
