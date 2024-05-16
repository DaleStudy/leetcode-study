- https://leetcode.com/problems/maximum-depth-of-binary-tree
- time complexity : O(n)
- space complexity : O(n), 단 입력 트리가 balanced되어 있다면 O(logn)
- https://algorithm.jonghoonpark.com/2024/02/18/leetcode-104

```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
```
