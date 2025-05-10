class Solution {
    public boolean isValidBST(TreeNode root) {
        return (root.left == null || isValidBSTMax(root.left, root.val))
                && (root.right == null || isValidBSTMin(root.right, root.val));
    }

    private boolean isValidBSTMax(TreeNode root, int max) {
        if (root.val >= max) {
            return false;
        }

        return (root.left == null || isValidBSTMax(root.left, root.val))
                && (root.right == null || isValidBSTMinMax(root.right, root.val, max));
    }

    private boolean isValidBSTMin(TreeNode root, int min) {
        if (root.val <= min) {
            return false;
        }

        return (root.left == null || isValidBSTMinMax(root.left, min, root.val))
                && (root.right == null || isValidBSTMin(root.right, root.val));
    }

    private boolean isValidBSTMinMax(TreeNode root, int min, int max) {
        if (root.val >= max || root.val <= min) {
            return false;
        }

        return (root.left == null || isValidBSTMinMax(root.left, min, root.val))
                && (root.right == null || isValidBSTMinMax(root.right, root.val, max));
    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
}
