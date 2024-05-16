- https://leetcode.com/problems/same-tree
- time complexity : O(n)
- space complexity : O(n), 단 입력 트리가 balanced되어 있다면 O(logn)
- https://algorithm.jonghoonpark.com/2024/03/31/leetcode-100

```java
public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }

        if (p == null || q == null) {
            return false;
        }

        return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```
