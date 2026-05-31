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
        /**
        1.문제: inverted binary tree 출력
        2.constraints: node 개수 min = 0, max = 100
        3.solution: left, right node swap
        time complexity: 
        - BST인 경우 best case : O(log n)
        - skwed 인 경우 worst case: O(n)
        - space complexity: O(h)
         */

         if(root == null) {
            return null;
         }

         dfs(root);

         return root;
        
    }

    void dfs(TreeNode root) {
        if(root == null) {
            return;
        }
        //swap
        TreeNode tmp = root.left;
        root.left = root.right;
        root.right = tmp;

        //left recursion
        dfs(root.left);
        //right recursion
        dfs(root.right);
    }
}
