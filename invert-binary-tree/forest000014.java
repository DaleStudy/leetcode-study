/*
# Time Complexity: O(n)
  - 전체 노드를 1번씩 탐색
# Space Complexity: O(n)
  - 재귀 호출의 각 depth마다 temp 노드 하나씩 생성
# Solution
  - 현재 노드의 왼쪽 자식과 오른쪽 자식을 각각 재귀 호출하여 자식의 자식 노드들을 반전시킨뒤,
  - 왼쪽 자식과 오른쪽 자식을 반전시킵니다.
  - base condition으로, 현재 노드가 null인 경우 null을 early return 합니다.
*/

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
        if (root == null) {
            return null;
        }

        invertTree(root.left);
        invertTree(root.right);

        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        return root;
    }
}
