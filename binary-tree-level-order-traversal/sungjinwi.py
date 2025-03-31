"""
    풀이 :
        level을 인자로 함께 넘겨서 level에 해당하는 인덱스에 append

    node 개수 N

    TC : O(N)
        모든 node에 대해 dfs호출

    SC : O(N)
        dfs 함수 호출 스택이 노드 개수 N만큼
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def dfs(node: Optional[TreeNode], level: int) -> None:
            if not node :
                return
            if len(ans) < level + 1 :
                ans.append([node.val])
            else:
                ans[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return ans
