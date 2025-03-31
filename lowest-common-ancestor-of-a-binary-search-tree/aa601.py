'''
TC: O(h) (h는 트리의 높이)
SC: O(1)
풀이 방법: 이진 탐색 트리의 성질을 이용해서 
		p,q의 값이 현재 노드 사이에 있거나 p,q의 값 중 하나라도 현재 노드와 같을 때까지 탐색한다
'''
# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		while root:
			if p.val < root.val and q.val < root.val:
				root = root.left
			elif p.val > root.val and q.val > root.val:
				root = root.right
			else:
				return root
