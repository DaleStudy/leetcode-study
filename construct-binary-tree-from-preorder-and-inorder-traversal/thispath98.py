# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Intuition:
            preorder 트리의 첫번째 원소는 항상 루트이다.
            또한, inorder 트리에서 루트를 기준으로 왼쪽은 left child,
            오른쪽은 right child를 의미한다.
            따라서 이를 이용해 재귀적으로 호출한다.

        Time Complexity:
            O(N^2):
                parent_idx를 선택하는 데에 O(N)이 소요되고
                최악의 경우 N번 재귀 호출해야 하므로 O(N^2)이다.

        Space Complexity:
            O(N):
                TreeNode는 N개의 값을 저장한다.

        Key takeaway:
            리트코드에서 클래스를 반환하는 문제는 다음처럼 하는 것을
            처음 알게 되었다.
        """
        if not preorder:
            return None

        parent = preorder[0]
        parent_idx = inorder.index(parent)  # O(N)

        left_pre = preorder[1 :parent_idx + 1]
        left_in = inorder[:parent_idx]
        left = self.buildTree(left_pre, left_in)

        right_pre = preorder[1 + parent_idx:]
        right_in = inorder[1 + parent_idx:]
        right = self.buildTree(right_pre, right_in)

        tree = TreeNode(parent, left, right)

        return tree
