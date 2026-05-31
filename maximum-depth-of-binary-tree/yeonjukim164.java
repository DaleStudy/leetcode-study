class Solution {
    public int maxDepth(TreeNode root) {
        // Base Case: 노드가 없으면 깊이는 0
        if (root == null) {
            return 0;
        }

        // Recursive Step: 왼쪽 깊이와 오른쪽 깊이 중 더 깊은 곳 + 1 (내 키)
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);

        return Math.max(leftDepth, rightDepth) + 1;
    }
}
