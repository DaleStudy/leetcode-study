
// dfs 방식으로 풀이해야 합니다. tree 관련 easy 문제를 10문제 정도 풀고 접근했습니다.
class Solution {
    public boolean isValidBST(TreeNode root) {
        return check(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean check(TreeNode node, long min, long max) {
        if (node == null) return true;

        if (!(node.val > min && node.val < max)) return false;

        return check(node.left, min, node.val) && check(node.right, node.val, max);
    }
}
