from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        - Time Complexity: O(n), n = The number of nodes in tree
        - Space Complexity: O(H), H = The height of tree,
            - H = logn, if the tree is balanced
            - H = n, if the tree is skewed
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # dfs : count the depth
        max_depth = 0
        
        def dfs(node, count):
            nonlocal max_depth
            
            if not node:
                max_depth = max(max_depth, count)
                return
            
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)
            
        dfs(root, 0)
        
        return max_depth        

def doTest():
    sol = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print("TC 1 is Success!" if sol.maxDepth(root1) == 3 else "TC 1 is Failed!")

    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    print(f"TC 2 is Success!" if sol.maxDepth(root2) == 2 else "TC 2 is Failed!")

    print(f"TC 3 is Success!" if sol.maxDepth(None) == 0 else "TC 3 is Failed!")
doTest()
