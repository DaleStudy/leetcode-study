/*
 * 시간복잡도 : O(n)
 */

class Solution {
    public boolean isValidBST(TreeNode root) {
        return valid(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    private boolean valid(TreeNode node, long min, long max) {
        if(node==null) return true;
        if(node.val <= min || node.val >=max) return false;
        return valid(node.left, min, node.val) && valid(node.right, node.val, max);
    }
}