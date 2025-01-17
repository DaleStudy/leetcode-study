# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
1) preorder 의 경우 젤 첫번째 노드가 최상단 노드라는 보장이 있음
2) inorder 의 경우 preorder 에서의 첫번째 node 를 기준으로 왼쪽이 left 노드, 오른찍이 right 노드라는 보장이 있음
3) preorder 에서 left, right의 갯수는 inorder에서 찾은 root node 의 인덱스 를 활용할 수 있음

Time: O(n^2)
Space: O(n^2)
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        newNode = TreeNode()
        newNode.val = preorder[0]
        mid = inorder.index(preorder[0])
        newNode.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        newNode.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return newNode

'''
알고달레 참고해서 최적화 진행했습니다.
1) 시간복잡도 최적화: dictionary 를 활용해 mid 를 찾는 index 메서드 제거
2) 공간복잡도 최적화: preorder, inorder 배열을 넘기는것이 아닌 index 만 넘김

Time: O(n)
Space: O(n)

'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = { val: idx for idx, val in enumerate(inorder) }
        pre_iter = iter(preorder)

        def dfs(start, end):
            if start > end:
                return None
            
            val = next(pre_iter)
            mid = indices[val]

            left = dfs(start, mid - 1)
            right = dfs(mid + 1, end)
            return TreeNode(val, left, right)

        return dfs(0, len(inorder) - 1)
