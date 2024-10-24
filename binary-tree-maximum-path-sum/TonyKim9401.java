// TC: O(n)
// visit all nodes to find maximum path
// SC: O(h)
// h means the high of binary tree
class Solution {
    private int output = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        max(root);
        return output;
    }

    private int max(TreeNode node) {
        if (node == null) return 0;

        int leftSum = Math.max(max(node.left), 0);
        int rightSum = Math.max(max(node.right), 0);

        int currentMax = node.val + leftSum + rightSum;

        output = Math.max(output, currentMax);

        return node.val + Math.max(leftSum, rightSum);
    }
}
