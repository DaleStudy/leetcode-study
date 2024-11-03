// TC: O(n)
// retreive all given nodes
// SC: O(1)
// doesn't require additional space
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null || q == null) {
            if (p == null && q == null) return true;
            return false;
        }

        if (p.val != q.val) return false;

        return isSameTree(p.left, q.left) &&
                isSameTree(p.right, q.right);
    }
}
