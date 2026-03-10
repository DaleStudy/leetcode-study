# time: O(n)
# space: O(h) : 추가 자료구조는 없지만 재귀 스택으로 인해 트리 높이만큼 공간 사용.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    answer = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root:
            if root.left:
                self.go_left(root.left, -2**31 - 1, root.val )
            if root.right:
                self.go_right(root.right, root.val, 2**31)

        return self.answer
    
    def go_left(self, cur:TreeNode, mm:int, MM:int):
        if mm >= cur.val or cur.val >= MM :
            self.answer = False
            return
        if cur.left:
            self.go_left(cur.left, mm, cur.val)
        if cur.right:
            self.go_right(cur.right, cur.val, MM)
    
    def go_right(self, cur:TreeNode, mm:int, MM:int):
        if mm >= cur.val or cur.val >= MM :
            self.answer = False
            return
        if cur.left:
            self.go_left(cur.left, mm, cur.val)
        if cur.right:
            self.go_right(cur.right, cur.val, MM)

        