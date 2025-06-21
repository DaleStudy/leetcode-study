from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        - Time Complexity: O(N), N = The number of nodes
        - Space complexity: O(H), H = The height of the tree
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

def build_tree(values):
    from collections import deque
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def tree_to_list(root):
    from collections import deque
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None
    while result and result[-1] is None:
        result.pop()
    return result

tc = [
        ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
        ([2,1,3], [2,3,1]),
        ([], [])
]

sol = Solution()
for i, (n, e) in enumerate(tc, 1):
    r = tree_to_list(sol.invertTree(build_tree(n)))
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
