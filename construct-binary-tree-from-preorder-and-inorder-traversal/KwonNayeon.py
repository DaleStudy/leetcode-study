"""
Constraints:
   1. 1 <= preorder.length <= 3000
   2. inorder.length == preorder.length 
   3. -3000 <= preorder[i], inorder[i] <= 3000
   4. preorder and inorder consist of unique values
   5. Each value of inorder also appears in preorder
   6. preorder is guaranteed to be the preorder traversal of the tree
   7. inorder is guaranteed to be the inorder traversal of the tree
   
Time Complexity:
   - O(N^2). 각 노드(N)마다 inorder에서 index를 찾는 연산(N)이 필요하고, 각 노드를 한 번씩 방문하여 트리를 구성하기 때문.
Space Complexity:
   - O(N). 재귀 호출 스택을 위한 공간이 필요하며, 최악의 경우(한쪽으로 치우친 트리) 재귀 깊이가 N까지 갈 수 있기 때문.
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
            
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
