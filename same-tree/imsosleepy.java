class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // 끝까지 내려왔으면 같다.
        if (p == null && q == null) return true;
        // 끝까지 내려왔는데, 값이 다르다.
        if (p == null || q == null || p.val != q.val) return false;
        // 양쪽 다 탐색
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
