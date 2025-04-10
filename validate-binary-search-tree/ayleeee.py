# 트리를 중위 순회하기 왼쪽 -> 루트 -> 오른쪽
# 이전에 방문한 노드의 값이 현재 값보다 작은지 확인
# 모든 노드가 조건 만족하면 True

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        # 최소값, 최대값 구할 때 사용
        # float('-inf') : 음의 무한대
        # float('inf') : 양의 무한대
        prev = float('-inf')
        current = root

        # current가 존재하거나 stack이 비어있지 않은 한 계속 지속
        while current or stack : 
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if current.val <= prev:
                return False
            prev = current.val
            current = current.right
        return True
            