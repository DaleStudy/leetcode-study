from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        - Time Complexity: O(n), n = The number of nodes
        - Space Complexity: O(H), H = The height of Tree
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            # Find max sum from the left and right children (more than 0)
            l_sum = max(dfs(node.left), 0)
            r_sum = max(dfs(node.right), 0)

            # Calculate current sum and update max_sum
            current_sum = node.val + l_sum + r_sum
            self.max_sum = max(self.max_sum, current_sum)

            # Return larger path
            return node.val + max(l_sum, r_sum)

        dfs(root)

        return self.max_sum
    
def do_test():
    sol = Solution()

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    e1 = 6
    r1 = sol.maxPathSum(root1)
    print(f"TC 1 is Passed!" if r1 == e1 else f"TC 1 is Failed! - Expected: {e1}, Result: {r1}")

    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    e2 = 42
    r2 = sol.maxPathSum(root2)
    print(f"TC 2 is Passed!" if r2 == e2 else f"TC 2 is Failed! - Expected: {e2}, Result: {r2}")

do_test()
