- https://leetcode.com/problems/kth-smallest-element-in-a-bst/
- time complexity : O(n)
- space complexity : O(n), 트리가 균등할 경우 O(logn)에 가까워진다.
- https://algorithm.jonghoonpark.com/2024/06/23/leetcode-230

```java
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        return dfs(root, new Holder(k));
    }

    public int dfs(TreeNode root, Holder holder) {
        if(root.left != null) {
            int left = dfs(root.left, holder);
            if (left != -1) {
                return left;
            }
        }
        holder.decrease();
        if (holder.k == 0) {
            return root.val;
        }
        if(root.right != null) {
            int right = dfs(root.right, holder);
            if (right != -1) {
                return right;
            }
        }
        return -1;
    }
}

class Holder {
    int k;

    public Holder(int k) {
        this.k = k;
    }

    public void decrease() {
        this.k = this.k - 1;
    }
}
```
