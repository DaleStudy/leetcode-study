"""
LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

summary:
전위순회(preorder)와 중위순회(inorder)를 기반으로 이진트리  구성하기
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # DFS
        # 시간복잡도 O(n), 공간복잡도 최악O(n)/평균O(log n) (n = 노드수)
        self.preorder_idx = 0   # preorder에 현재 위치 인덱스(처음값 = 루트노드값)

        inorder_map = {}    # inorder 값을 인덱스로 매핑(빠른 검색을 위해)
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i


        def dfs(left: int, right:int) -> Optional[TreeNode]:
            # 왼쪽인덱스가 오른쪽인덱스보다 크면(범위를벗어나면) 빈 서브트리 -> 종료
            if left > right:
                return None

            # 현재 preorder에서 현재 루트 값 가져오고 한 칸 이동
            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1

            # 루트 노드 생성
            root = TreeNode(root_val)

            # inorder에서 현재 루트 위치 찾기
            i = inorder_map[root_val]

            # 왼쪽, 오른쪽 서브트리 구성
            root.left = dfs(left, i-1)
            root.right = dfs(i+1, right)

            return root

        # 전체 inorder dfs 돌기
        return dfs(0,len(inorder)-1)
