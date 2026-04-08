# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        시간복잡도: O(n)
        공간복잡도: O(n)
        이진 트리 탐색하며 뎁스 증가 계속 하며 진행
        """
        depth = 0
        if not root:
            return 0
        array = [(root, 1)]
        while array:
            node, d = array.pop()
            depth = max(d, depth)
            if node.left:
                array.append((node.left, d + 1))
            if node.right:
                array.append((node.right, d + 1))
        return depth
