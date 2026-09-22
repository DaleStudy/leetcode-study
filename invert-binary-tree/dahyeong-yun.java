/**
 * TC : O(n)
 *   - 모든 노드를 방문해야 함
 * SC : O(n)
 *   - 콜 스택이 n까지 쌓일 수 있음
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return root;

        // 다음에 다음이 있는 경우만 스왑해서 리턴
        if(root.left != null || root.right != null) {
            TreeNode temp = invertTree(root.left);
            root.left = invertTree(root.right);
            root.right = temp;
        }

        return root;
    }
}
