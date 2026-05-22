from collections import deque

# 7기 풀이
# 시간 복잡도: O(n)
# - 모든 노드를 순회하여 serialize / deserialize 하므로 노드의 개수만큼 시간 소요
# 공간 복잡도: O(n)
# - 모든 노드에 대한 값을 list에 넣어 사용하므로 노드의 개수만큼 공간 사용
class Codec:
    DELIMITER = "$"  # serialize할 때 노드의 값을 구분하기 위한 구분자
    NONE_VALUE = "N"  # serialize할 때 노드가 None인 경우를 구분하기 위한 구분자

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []  # node의 값들을 저장할 list 추가

        def dfs(node):
            if not node:
                # node가 None인 경우에는 None 구분자를 저장
                data.append(self.NONE_VALUE)
                return

            data.append(str(node.val))  # node가 있는 경우에 val를 data에 저장

            dfs(node.left)  # 왼쪽 자식 노드 탐색
            dfs(node.right)  # 오른쪽 자식 노드 탐색

        dfs(root)  # 전체 트리 탐색
        return f"{self.DELIMITER}".join(data)  # 탐색하여 저장한 data list를 구분자를 이용해 string으로 변환하여 return

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        data = deque(data.split(self.DELIMITER))  # string 값을 구분자를 기준으로 split 한 후 deque에 저장

        def dfs():
            val = data.popleft()  # data 값 중 가장 왼쪽에 있는 값을 pop
            if val == self.NONE_VALUE:
                # None 구분자의 값이 나온 경우에는 node가 없었던 것이므로 None 리턴
                return None

            node = TreeNode(val)  # 노드 생성
            node.left = dfs()  # 왼쪽 자식 노드 생성
            node.right = dfs()  # 오른쪽 자식 노드 생성

            return node  # 완성한 노드 return

        root = dfs()
        return root
