/*
 * time: O(N)
 * space: O(N)
 */
class Solution {

    List<Integer> inorderList = new ArrayList<>();

    public int kthSmallest(TreeNode root, int k) {
        inorder(root);
        return inorderList.get(k - 1);
    }

    public void inorder(TreeNode cur) {
        if (cur == null) {
            return;
        }
        inorder(cur.left);
        inorderList.add(cur.val);
        inorder(cur.right);
    }
}
