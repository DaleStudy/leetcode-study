/**
 * 최대 depth 까지 가봐야 하므로 DFS 탐색 이용 
 * 
 * 모든 노드를 순회해야 하므로 시간복잡도 O(N)
 * 재귀 호출 스택 프레임 (= 트리 최대 높이 height) 만큼 공간복잡도 O(H)
 * 
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
        if (root == null) return 0; // 자식이 없으면 종료

        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        return Math.max(left, right) + 1; // 루트는 기본 1층이니까 1 더한다
    }
}
