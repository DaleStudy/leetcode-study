from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        
        q = deque([(root, 0)])

        while q:
            node, depth = q.popleft()
            if not node:
                continue
            
            if len(answer)-1 < depth:
                answer.append([])
 
            answer[depth].append(node.val)

            q.append((node.left, depth+1))
            q.append((node.right, depth+1))

        return answer
    
