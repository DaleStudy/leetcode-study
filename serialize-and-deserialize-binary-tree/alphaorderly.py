# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
# 시간 복잡도: O(n)
# 공간 복잡도: O(n)
#
# 이 코드는 preorder(전위 순회)를 이용해 이진 트리를 문자열로 직렬화하고,
# 다시 preorder 순서로 문자열을 역직렬화하여 트리를 복원한다.
#
# 1. serialize 함수는 preorder 순회로 트리 노드를 방문하며 값을 문자열로 저장하고,
#    None 자리는 특수문자(*)로 표기한다.
# 2. deserialize 함수는 preorder 순서의 문자열을 한 항목씩 읽어가며
#    *이면 None, 숫자면 그 값의 TreeNode를 재귀적으로 생성한다.
"""
class Codec:

    def serialize(self, root):
        ans = []

        def preorder(node: Optional[TreeNode]):
            if not node:
                ans.append("*")
                return

            ans.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ','.join(ans)

    def deserialize(self, data):
        data = iter(data.split(','))

        def preorder() -> TreeNode:
            current = next(data)

            if current == '*':
                return None

            node = TreeNode(int(current))
            node.left = preorder()
            node.right = preorder()

            return node

        return preorder()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
