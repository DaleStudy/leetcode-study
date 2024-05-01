- https://leetcode.com/problems/invert-binary-tree/
- time complexity : O(n)
- space complexity : O(log n)
- https://algorithm.jonghoonpark.com/2024/03/31/leetcode-226

```java
public class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }

        var temp = root.left;
        root.left = root.right;
        root.right = temp;

        if (root.left != null) {
            invertTree(root.left);
        }
        if (root.right != null) {
            invertTree(root.right);
        }

        return root;
    }
}
```
