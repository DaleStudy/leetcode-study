# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(arr):
    if not arr:
        return None
#      -> 레벨로 주고 있음
    root = TreeNode(arr[0])
    queue = deque([root]) # 큐에 root를 넣고 시작 queue = deque() queue.append(root)와 동일
    i = 1

    while queue and i < len(arr):
        current = queue.popleft()

        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1

    return root


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        def inorder(node):
            if not node:
                return True

            # 왼쪽 서브트리 확인
            if not inorder(node.left):
                return False

            # 현재 노드 값 확인
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val

            return inorder(node.right)

        return inorder(root)