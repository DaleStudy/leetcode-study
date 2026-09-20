# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

"""
문제:
    - 이진 트리의 root가 주어질 때, 노드 값을 레벨 순서(왼쪽에서 오른쪽, 위에서 아래)로 묶어서 반환한다
    - 결과는 레벨별 값 리스트의 리스트 (예: [[3], [9, 20], [15, 7]])
    - 0 <= 노드 수 <= 2000

복잡도:
    n: 노드의 개수
    Time: O(n)
    Space: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        ans = []
        q = deque([(0, root)])
        while q:
            level, node = q.popleft()
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))

        return ans
