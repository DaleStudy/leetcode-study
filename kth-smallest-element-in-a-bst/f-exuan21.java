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
    private TreeNode resultNode = null;

    public int kthSmallest(TreeNode root, int k) {
        searchNode(root, k);
        return resultNode.val;
    }

    public void searchNode(TreeNode node, int k) {

        if(resultNode != null) return;

        if(node.left != null) {
            searchNode(node.left, k); 
        }

        count++;

        if(count == k) {
            resultNode = node;
            return;
        }

        if(node.right != null) {
            searchNode(node.right, k);
        }
    }
}

// n : 노드 개수
// time : O(n) 최악의 경우 모든 노드를 탐색해야함
// space : O(n) 최악의 경우 한 쪽으로 노드가 치우쳐져 있음 
// -> 재귀 호출이 이루어지므로 스택에 쌓임 -> 한 쪽으로 쏠려 있으면 트리의 높이가 n이 됨 (트리의 최대 높이가 스택의 최대 깊이)
