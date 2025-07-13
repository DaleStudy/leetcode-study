/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // subtree null일 경우
        if (subRoot == null) {
            return true;
        }
        // 이진 트리가 null일 경우
        if (root == null) {
            return false;
        }
        // subtree라면
        if (isIdentical(root, subRoot)) {
            return true;
        }

        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);

    }

    //  isIdentical(s,t)= s.val==t.val AND isIdentical(s.left,t.left) AND isIdentical(s.right,t.right)
    private boolean isIdentical(TreeNode r, TreeNode s) {
        if (r == null || s == null) {
            return r == null && s == null;
        }
        if (r.val != s.val) {
            return false;
        }
        return isIdentical(r.left, s.left) && isIdentical(r.right, s.right);
    }
}

