class Solution {

  public TreeNode invertTree(TreeNode root) {
    if (root == null) {
      return null;
    }

    TreeNode tmp = root.left;
    root.left = root.right;
    root.right = tmp;

    invertTree(root.right);
    invertTree(root.left);

    return root;
  }

}
