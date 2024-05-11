/**
 * 달레님 강의 참고
 * 아직 완벽하게 이해하지 못한 풀이,, 추가로 다시 확인 필요
 * 시간복잡도: O(n)
 * 공간복잡도: O(n)
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        invertTree(root.right);
        invertTree(root.left);

        return root;
    }
}
