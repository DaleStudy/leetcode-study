"""
[Problem]
https://leetcode.com/problems/validate-binary-search-tree/

[Brainstorming]
BST가 유효한지를 검증하는 문제.
1 <= number of nodes <= 10^4(100,000)

[Plan]
1. Tree를 DFS를 이용하여 만든다.
2. 실제로 입력을 넣어보며, 존재하지 않는 경우 False를 반환한다.
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Attempt 1 - My Solution (incorrect)
    이 풀이의 경우, 자기 자신과 자기 자식 노드들 까지만으로 한정한다.
    따라서, BST를 제대로 검증할 수 없다.
    root = [5,4,6,null,null,3,7] 인 경우에는 검증할 수 없다. (Edge Case)
    """
    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        invalid_flag = False
        def dfs(node:Optional[TreeNode])->None:
            nonlocal invalid_flag
            if invalid_flag:
                return

            if not node:
                return

            if node.left and node.left.val > node.val:
                invalid_flag = True
                return
            if node.right and node.right.val < node.val:
                invalid_flag = True
                return

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return not invalid_flag
    """
    Attempt 2 - Another Solution
    ref: https://www.algodale.com/problems/validate-binary-search-tree
    [Complexity]
    N: number of nodes in trees
    Time: O(N) => Traverse all nodes in the tree.
    Space: worst case: O(N), best case: O(log N)
    """

    def isValidBST(self, root:Optional[TreeNode])->bool:
        def dfs(node:Optional[TreeNode], min_limit:int, max_limit:int)->bool:
            if not node:
                return True
            if not (min_limit < node.val < max_limit):
                return False

            return dfs(node.left, min_limit, node.val) and dfs(node.right, node.val, max_limit)


