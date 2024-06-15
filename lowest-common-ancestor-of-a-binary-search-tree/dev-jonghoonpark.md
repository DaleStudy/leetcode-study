- 문제: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
- time complexity : O(n)
- space complexity : O(n), 트리가 균등한 형태일 경우 O(logn)에 가까워진다.
- 블로그 링크 : https://algorithm.jonghoonpark.com/2024/06/10/leetcode-235

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return dfs(root, p, q);
    }

    private TreeNode dfs(TreeNode node, TreeNode p, TreeNode q) {
        if (node == null) {
            return null;
        }

        TreeNode left = dfs(node.left, p, q);
        TreeNode right = dfs(node.right, p, q);

        if ((left != null && right != null) || node.val == p.val || node.val == q.val) {
            return node;
        }

        return left != null ? left : right;
    }
}
```
