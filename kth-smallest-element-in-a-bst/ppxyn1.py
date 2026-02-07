# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#idea : DFS (inorder)
#Time Complexity: O(n)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cnt = 0
        curr = root 
        if not curr:
            return

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left 
            curr = stack.pop()
            cnt += 1

            if cnt == k:
                return curr.val
            
            curr = curr.right 

