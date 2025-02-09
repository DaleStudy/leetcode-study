from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# 시간 복잡도 : O(n)
# 공간 복잡도 : O(n)
class Solution:
	# 오른쪽부터 탐색하는 전위 순회 구현
	def invertPreOrder(self, src: TreeNode, des: TreeNode) -> None:
		des.val = src.val
		if src.right:
			des.left = TreeNode()
			self.invertPreOrder(src.right, des.left)
		if src.left:
			des.right = TreeNode()
			self.invertPreOrder(src.left, des.right)
		
	def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		if not root:
			return None
		des = TreeNode()
		self.invertPreOrder(root, des)
		return des

