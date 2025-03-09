'''
TC: O(n)
SC: O(n)
'''

class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		# 재귀함수 호출 시 노드가 존재하지 않을 때 탈출한다
		if not root:
			return 0
		# root를 기준으로 왼쪽 서브트리, 오른쪽 서브트리를 재귀호출로 쌓아놓고 리프노드부터 세면서 트리의 깊이를 구한다
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 
