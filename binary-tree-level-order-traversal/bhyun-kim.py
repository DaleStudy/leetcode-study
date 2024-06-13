"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Solution 
    Breadth First Search (BFS) using Queue

    The problem is asking to return the node values at each level of the binary tree.
    To solve this problem, we can use BFS algorithm with a queue.
    We will traverse the tree level by level and store the node values at each level.

    1. Initialize an empty list to store the output.
    2. Initialize an empty queue.
    3. Add the root node to the queue.
    4. While the queue is not empty, do the following:
        - Get the size of the queue to know the number of nodes at the current level.
        - Initialize an empty list to store the node values at the current level.
        - Traverse the nodes at the current level and add the node values to the list.
        - If the node has left or right child, add them to the queue.
        - Decrease the level size by 1.
        - Add the list of node values at the current level to the output.
    5. Return the output.

Time complexity: O(N)
    - We visit each node once

Space complexity: O(N)
    - The maximum number of nodes in the queue is the number of nodes at the last level
    - The maximum number of nodes at the last level is N/2
    - The output list stores the node values at each level which is N
    - Thus, the space complexity is O(N)

"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        output = []
        queue = []
        queue.append(root)

        while(len(queue) > 0):
            level_size = len(queue)
            level_output = []
            
            while level_size > 0:
                node = queue.pop(0)
                level_output.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right) 

                level_size -= 1

            output.append(level_output)

        return output
