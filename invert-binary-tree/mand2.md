### Intuition
- 재귀호출

### Approach
- 재귀 호출
- 마지막에 left<>right 이동

### Complexity
- Time complexity: O(n)
- Space complexity: O(n)


# Code

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left
        
        return root

        
```
