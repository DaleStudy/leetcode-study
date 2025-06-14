# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        [Complexity]
            - TC: O(n) (각 node를 한 번씩 방문)
            - SC: O(height) (tree의 높이만큼 call stack)

        [Approach]
            path에는 같은 node가 두 번 들어갈 수 없으므로, 각 node 마다 해당 node를 지난 path의 max sum은 다음과 같이 구할 수 있다.
                = (1) left child를 지나는 path의 max_sum
                  + (2) right child를 지나는 path의 max_sum
                  + (3) 현재 node의 val
            따라서 이는 재귀 문제로 풀 수 있으며, 각 단계마다 global max sum과 비교하며 값을 업데이트 하면 된다.

            이때 node의 값은 음수가 될 수 있으므로, (1) & (2)가 음수라면 0으로 처리해야 한다. 즉,
                = (1) max(get_max_sum(node.left), 0)
                  + (2) max(get_max_sum(node.right), 0)
                  + (3) 현재 node의 val
            과 같이 구하고, global max sum과 이 값을 비교하면 된다.

            또한, 현재 보고 있는 node가 get_max_sum() 함수의 반환값은
                = 현재 node의 값 + (1) & (2) 중 큰 값
            이어야 한다. 왜냐하면 현재 node를 두 번 이상 방문할 수 없기 때문이다.
        """

        res = -1001

        def get_max_sum(node):
            """주어진 node가 root인 tree에서, root를 지나는 path의 max sum을 구하는 함수"""
            nonlocal res

            # base condition
            if not node:
                return 0

            # compute left & right child's max path sum
            left_max_sum = max(get_max_sum(node.left), 0)
            right_max_sum = max(get_max_sum(node.right), 0)

            # compute max path sum at this step
            max_sum = left_max_sum + right_max_sum + node.val

            # update res
            res = max(res, max_sum)

            return node.val + max(left_max_sum, right_max_sum)

        get_max_sum(root)

        return res
