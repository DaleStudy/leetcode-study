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
    int maxValue = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        /**
        1.노드의 sum이 가장 최대가 되는 path 의 maximum sum 찾기
        2.solution : DFS
         */
         
        dfs(root);
        return maxValue;
        
    }

    private int dfs(TreeNode node) {
        if(node == null) {
            return 0;
        }

        int left = Math.max(0, dfs(node.left));
        int right = Math.max(0, dfs(node.right));

        //현재 노드를 중심으로하는 Path
        int currPath = left + node.val + right;

        //update max value
        maxValue = Math.max(maxValue, currPath);

        //부모 노드에게 최대값 전달
        return node.val + Math.max(left, right);
    }
    
}
