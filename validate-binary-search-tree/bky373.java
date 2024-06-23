/**
 * time: O(N)
 * space: O(N)
 */
class Solution {

    public boolean isValidBST(TreeNode root) {
        return dfs(root, null, null);
    }

    public boolean dfs(TreeNode cur, Integer low, Integer high) {
        if (cur == null) {
            return true;
        }
        if (low != null && cur.val <= low) {
            return false;
        }
        if (high != null && cur.val >= high) {
            return false;
        }
        return dfs(cur.left, low, cur.val) && dfs(cur.right, cur.val, high);
    }
}
