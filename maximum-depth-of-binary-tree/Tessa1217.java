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
/**
 * 이진 트리의 루트가 주어질 때 최대 깊이를 구하세요.
 */
class Solution {

    int maxDepth = 0;

    // 시간 복잡도: O(n)
    public int maxDepth(TreeNode root) {
        depthChk(root, 0);
        return maxDepth;
    }

    // 재귀로 풀이 진행
    public void depthChk(TreeNode node, int depth) {
        // 탐색할 노드 없을 경우
        if (node == null) {
            maxDepth = Math.max(depth, maxDepth);
            return;
        }
        // 트리의 좌우 탐색
        depthChk(node.left, depth + 1);
        depthChk(node.right, depth + 1);
    }
}

