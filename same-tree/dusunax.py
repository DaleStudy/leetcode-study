'''
# 100. Same Tree

## Base case
- if both nodes are None, return True
- if one of the nodes is None, return False
- if the values of the nodes are different, return False

## Recursive case
- check if the left subtrees are the same
- check if the right subtrees are the same

## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

#### TC is O(n):
- visiting each node once, balanced or skewed, it's O(n)

#### SC is O(n):
- for h is tree's height.
  - in best case(balanced): h is logN, so SC is O(logN)
  - in worst case(skewed): h is N, so SC is O(N)
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
