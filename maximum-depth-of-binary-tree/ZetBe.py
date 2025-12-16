'''
문제: 이진 트리의 최대 깊이를 구하시오.
풀이: 깊이 우선 탐색(DFS)을 사용하여 트리의 각 경로를 탐색하고, 최대 깊이를 갱신합니다.
시간 복잡도: O(n), n은 트리의 노드 수입니다. 모든 노드를 한 번씩 방문하므로 전체 시간 복잡도는 O(n)입니다.
공간 복잡도: O(h), h는 트리의 높이입니다. 재귀 호출 스택이 최대 h 깊이까지 쌓일 수 있으므로 공간 복잡도는 O(h)입니다.
사용한 자료구조: 함수(재귀 호출 스택)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        answ = 1
        def dfs(root, a):
            nonlocal answ
            if root.left:
                dfs(root.left, a+1)
            if root.right:
                dfs(root.right, a+1)
            answ = max(answ, a)
            return a
        dfs(root, 1)
        return answ


