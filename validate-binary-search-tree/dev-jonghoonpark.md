- 문제 : https://leetcode.com/problems/validate-binary-search-tree/
- time complexity : O(n)
- space complexity : O(n), 트리가 균등한 형태일 경우 O(logn)에 가까워진다.
- 블로그 링크 : https://algorithm.jonghoonpark.com/2024/06/10/leetcode-98

```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return dfs(root.left, (long) Integer.MIN_VALUE - 1, root.val)
               && dfs(root.right, root.val, (long) Integer.MAX_VALUE + 1);
    }

    private boolean dfs(TreeNode node, long min, long max) {
        if (node == null) {
            return true;
        }

        // left로 갈 때 max를 자신으로, right로 갈 때는 min을 자신으로
        if (!(dfs(node.left, min, node.val)
              && dfs(node.right, node.val, max))) {
            return false;
        }

        return node.val > min && node.val < max;
    }
}
```
