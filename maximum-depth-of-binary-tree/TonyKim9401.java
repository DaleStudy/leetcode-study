// TC: O(n)
// visiting all nodes
// SC: O(1)
// constant space complexity
class Solution {
    public int maxDepth(TreeNode root) {
        return getMax(root, 0);
    }

    private int getMax(TreeNode node, int depth) {
        if (node == null) return depth;
        depth += 1;
        return Math.max(getMax(node.left, depth), getMax(node.right, depth));
    }
}
