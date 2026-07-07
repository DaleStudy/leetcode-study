import java.util.*;

// TC: O(n)
// SC: O(h)
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValid(root, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
    }

    private boolean isValid(TreeNode node, double min, double max) {
        if (node == null) {
            return true;
        }
        if (node.val <= min || node.val >= max) {
            return false;
        }
        return isValid(node.left, min, node.val) && isValid(node.right, node.val, max);
    }
}
