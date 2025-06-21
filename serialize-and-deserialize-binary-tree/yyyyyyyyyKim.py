# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # DFS

    # 이진트리 -> 문자열 변환(직렬화)
    # 시간복잡도 O(n), 공간복잡도 O(n)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null'

        # 재귀 호출로 노드값을 문자열로 저장
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)
        

    # 문자열 -> 이진트리 변환(역직렬화)
    # 시간복잡도 O(n), 공간복잡도 O(n)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # ','를 기준으로 끊어서 리스트로 변환
        s = data.split(',')

        def dfs():
            # 맨 앞부터 꺼내기
            val = s.pop(0)
            
            # null이면 자식 노드 없음
            if val == 'null':
                return None
            
            node = TreeNode(int(val))   # 현재 노드
            node.left = dfs()           # 왼쪽 서브트리
            node.right = dfs()          # 오른쪽 서브트리

            return node

        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
