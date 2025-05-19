class Solution {
    public int maxVal;
    public int maxDepth(TreeNode root) {
        dfs(root, 0);
        return maxVal;
    }
    public void dfs(TreeNode node, int step) {

        if (node == null) {
            if (maxVal < step) maxVal = step;
            return;
        }

        dfs(node.left, step + 1);
        dfs(node.right, step + 1);
    }
}
