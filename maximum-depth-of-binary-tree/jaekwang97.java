class Solution {
    private int max;

    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        max = 0;
        dfs(root, 1);

        return max;
    }

    private void dfs(TreeNode node, int depth) {
        if (node == null) {
            return;
        }

        max = Math.max(max, depth);

        dfs(node.left, depth + 1);
        dfs(node.right, depth + 1);
    }
}
