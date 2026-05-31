'''
문제: 이진 탐색 트리가 유효한지 확인하기
풀이: 깊이 우선 탐색(DFS)을 사용하여 각 노드가 유효한 범위 내에 있는지 확인
시간복잡도: O(n)
    모든 노드를 한 번씩 방문하므로 전체 시간복잡도는 O(n)이다.
공간복잡도: O(h)
    재귀 호출 스택이 트리의 높이 h에 비례하므로 전체 공간복잡도는 O(h)이다.
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, ma, mi):
            if root == None:
                return True

            if not (mi < root.val < ma):
                return False
            
            return dfs(root.left, root.val, mi) and dfs(root.right, ma, root.val)
            
        a = dfs(root, 10**100, -1*(10**100))
        return a

