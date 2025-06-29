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

    private int kthSmallValue = 0;

    // 시간복잡도: O(k) (불균형 상태의 이진 트리일 경우 O(n))
    public int kthSmallest(TreeNode root, int k) {
        orderSearch(root, k);
        return kthSmallValue;
    }

    // In Order Search
    private void orderSearch(TreeNode node, int k) {

        if (node == null) {
            return;
        }

        // HINT => utilize the property of a BST => 좌측 리프 노드부터 탐색
        orderSearch(node.left, k);

        count++;

        if (count == k) {
            kthSmallValue = node.val;
            return;
        }

        // search right side
        orderSearch(node.right, k);

    }

}

