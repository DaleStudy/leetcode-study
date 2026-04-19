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
 import java.util.*;
class Solution {
    private static int solve(TreeNode root, int depth){
        if (root == null){
            return depth;
        }

        //root가null이 아닌 경우
        return Math.max(solve(root.left, depth+1) , solve(root.right, depth+1));

    }
    public int maxDepth(TreeNode root) {
        int result = solve(root, 0);
        return result;
    }
}

