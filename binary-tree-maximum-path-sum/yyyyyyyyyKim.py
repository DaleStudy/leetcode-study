# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # DFS + 분할정복형 DP
        # 시간복잡도 O(n), 공간복잡도 O(n)
        self.answer = float('-inf')  # 최저값을 초기값으로 세팅(dfs함수에서도 쓰일 수 있게 인스턴스변수 선언해서 전역변수처럼 사용)

        def dfs(node):
            if not node:
                return 0

            # 왼쪽, 오른쪽 서브트리에서 최대합(음수라면 버리고 0 가져가기)
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))
   
            # 현재 노드를 포함하는 최대합으로 answer 업데이트
            self.answer = max(self.answer, left + right + node.val)

            # 왼쪽,오른쪽 중 최대값 선택(한방향이니까)해서 부모에게 리턴
            return max(left, right) + node.val


        dfs(root)
        return self.answer
