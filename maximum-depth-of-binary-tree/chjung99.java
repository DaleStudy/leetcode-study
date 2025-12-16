import java.util.*;

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
    class Data{
        TreeNode node;
        int depth;
        public Data(TreeNode node, int depth){
            this.node = node;
            this.depth = depth;
        }
    }
    public int maxDepth(TreeNode root) {
        return bfs(root);
    }
    public int bfs(TreeNode root) {
        int depth = 0;
        Queue<Data> q = new ArrayDeque<>();
        if (root != null){
            q.add(new Data(root, 1));
        }
        while (!q.isEmpty()){
            Data cur = q.poll();
            if (cur.depth > depth){
                depth = cur.depth;
            }
            if (cur.node.left != null) {
                q.add(new Data(cur.node.left, cur.depth + 1));
            }
            if (cur.node.right != null) {
                q.add(new Data(cur.node.right, cur.depth + 1));
            }
        }
        return depth;
    }
}

