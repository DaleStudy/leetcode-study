# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# preorder -> root, left, right
# inorder -> left, root, right

# Ex1 [3,9,20,null,null,15,7]
# preorder -> root-1, left, (root-2 - root, left, right)
# inorder -> left, root-1, (root-2 - left, root, right)

# Ex2 [-1]
# preorder -> root, left(x), right(x)
# inorder -> left(x), root, right(x)

# Ex3 [3,9,20,11,8,15,7]
# preorder -> root-1, (root-2(left) - root, left, right), (root-3(right) - root, left, right)
# [3,9,11,8,20,15,7]
# inorder -> (root-1(left) - left, root, right), root-2, (root-3(right) - left, root, right)
# [11, 9, 8, 3, 15, 20, 7]

# Ex4 [3,9,20,11,8]
# preorder -> root-1, (root-2(left) - root, left, right), (root-3(right) - root)
# [3,9,11,8,20]
# inorder -> (root-1(left) - left, root, right), root-2, (root-3(right) - left(X), root)
# [11, 9, 8, 3, 20]

# 문제풀이 : divide and conquer
# preorder의 첫번째 요소를 가지고 inorder split
# split된 left와 right의 개수에 맞게 preorder을 두 번 째 원소부터 순서대로 할당
# 예) left 원소 개수 : 3 -> preorder[1:1+3], right 원소 개수 : 2 -> preorder[1+3:]
# left, right 각각 buildTree로 넣기

"""
복잡도 : 예상 -> 예상한 이유

시간 복잡도 : O(n) -> 분할해서 처리하지만, 모든 노드를 방문하므로
공간 복잡도 : O(n) -> 입력 배열만큼의 길이와 거의 동일한 배열이 생성되므로
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])

        split_idx = inorder.index(preorder[0])
        left_inorder = inorder[:split_idx]
        right_inorder = inorder[split_idx+1:]
        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1:]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root

