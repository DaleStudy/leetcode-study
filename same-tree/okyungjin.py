"""
https://leetcode.com/problems/same-tree/description/

N: min(p노드수, q노드수)
Time: O(N)
Space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])

        while queue:
            node_p, node_q = queue.popleft()

            if not node_p and not node_q:
                continue

            elif node_p and node_q:
                if node_p.val == node_q.val: 
                    queue.append((node_p.left, node_q.left))
                    queue.append((node_p.right, node_q.right))
                else:
                    return False
            
            else:
                return False

        return True
