/**
 * time: O(n)
 * space: O(n)
 */

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
    public TreeNode invertTree(TreeNode root) {
        breadthFirstSearch(root);
        return root;
    }
    public void breadthFirstSearch(TreeNode node){
        Deque<TreeNode> queue = new ArrayDeque<>();
        if (node != null){
            queue.add(node);
        }

        while (!queue.isEmpty()){
            TreeNode cur = queue.remove();

            TreeNode tmp = cur.left;
            cur.left = cur.right;
            cur.right = tmp;

            if (cur.left != null){
                queue.add(cur.left);
            }
            if (cur.right != null){
                queue.add(cur.right);
            }
        }
    }
}

