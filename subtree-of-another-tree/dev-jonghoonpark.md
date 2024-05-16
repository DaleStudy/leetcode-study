- https://leetcode.com/problems/subtree-of-another-tree
- root tree 의 노드 수를 n, sub tree 의 노드 수를 m 이라고 하였을 때
  - time complexity : O(n \* m)
  - space complexity : O(n + m), 단 입력 트리가 balanced되어 있다면 O(logn + logm)
- https://algorithm.jonghoonpark.com/2024/05/14/leetcode-527

```java
public class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) {
            return true;
        }

        if (root == null || subRoot == null) {
            return false;
        }

        if (isSubtreeStrict(root, subRoot)) {
            return true;
        }

        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    public boolean isSubtreeStrict(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) {
            return true;
        }

        if (root == null || subRoot == null) {
            return false;
        }

        return root.val == subRoot.val && isSubtreeStrict(root.left, subRoot.left) && isSubtreeStrict(root.right, subRoot.right);
    }
}
```
