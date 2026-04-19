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
    public int maxDepth(TreeNode root) {
        /**
        문제: 바이너리트리의 maximum depth 구하기
        조건
        - 노드의 개수는 0 ~ 10^4
        - node val 은 -100 ~ 100
        풀이: dfs 로 depth 구하기
        - 주어진 트리는 binary tree
        - time complexity : O(n) , O(log n)
        - space complexity : O(h)
         */


         if(root == null) return 0;

         int height = dfs(root);
        return height;
    }

    int dfs(TreeNode node) {
        if(node == null) return 0;

        int left = dfs(node.left);
        int right = dfs(node.right);

        return Math.max(left, right) + 1;
    }
}
