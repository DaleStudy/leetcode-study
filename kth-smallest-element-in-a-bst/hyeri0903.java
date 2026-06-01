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
    private int count = 0;
    private int answer = 0;
    public int kthSmallest(TreeNode root, int k) {
        /**
        1.BST에서 K번째 가장 작은 값 찾기
        2.constraints : node 개수 ㅡin = 0, max = 10000
        3.solutions:
        - k번째 방문한 노드가 k번째로 작은 값 (bst 이므로)
        - dfs search (inorder traversal)
         */
    
         dfs(root, k);
         return answer;
    }
    private void dfs(TreeNode node, int k) {
        if(node == null) {
            return;
        }

        
        dfs(node.left, k);
        count++;

        if(count == k) {
            answer = node.val;
            return;
        }
        
        dfs(node.right, k);
    }
   
}
