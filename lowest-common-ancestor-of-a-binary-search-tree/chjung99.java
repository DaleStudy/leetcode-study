/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode node = root;

        while (true) {
            if (node == null) break;
            int pDir = findDir(node.val, p.val);
            int qDir = findDir(node.val, q.val);
            if (pDir == 0 || qDir == 0) return node;
            if (pDir != qDir) return node;
            if (qDir == -1) {
                node = node.left;
            } else {
                node = node.right;
            }
        }
        return node;
    }

    public int findDir(int nodeVal, int targetVal) {
        if (nodeVal < targetVal) return 1;
        if (nodeVal == targetVal) return 0;
        if (nodeVal > targetVal) return -1;
        return -2;
    }
}


