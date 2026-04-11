# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """주어진 binary tree의 최대 깊이를 찾는 함수

        방법:
        1. 재귀함수를 생각함. 인자로 현재 head node와 현재의 depth를 받는 재귀함수를 만들어 재귀 반복
        2. 이 함수 자체가 재귀가 될 수 있다고 판단, 별도의 재귀함수를 삭제함.
            depth를 넘겨주지 않아도, 앞에 +1을 함으로써 depth가 계산됨.

        Args:
            root (TreeNode | None): binary tree

        Returns:
            int: 최대 깊이
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
