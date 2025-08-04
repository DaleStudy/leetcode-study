class TreeNode {
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

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {

        if (p == null && q == null) {
            return true;
        }

        if (p == null || q == null || q.val != p.val) {
            return false;
        }

        // 특정 깊이의 Node 가 같다면 null을 만날때 까지 탐색하고, 같지 않다면 바로 false를 반환.
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
