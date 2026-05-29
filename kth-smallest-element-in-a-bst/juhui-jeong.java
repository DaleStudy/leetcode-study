/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> list = new ArrayList<>();
        inorder(root, list);

        return list.get(k-1);
    }
    private void inorder(TreeNode node, List<Integer>list) {
        if (node == null) return;

        inorder(node.left, list);
        list.add(node.val);
        inorder(node.right, list);
    }
}
