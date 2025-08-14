class Solution {
    /*
     * 시간복잡도: O(n)
     */
    public int maxDepth(TreeNode root) {
        if(root==null) return 0;
        return 1+Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}

