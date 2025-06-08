# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # 이진트리 뒤집기(좌우반전)
        # DFS(stack이용, 시간복잡도 O(n), 공간복잡도 O(n))
        if not root:
            return None

        stack = [root]

        while stack:
            # 스택 맨뒤에 있는 거 pop해서 꺼내기
            node = stack.pop()

            # 자식 노드 교환
            node.left, node.right = node.right, node.left

            # 자식 노드를 스택에 추가
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
