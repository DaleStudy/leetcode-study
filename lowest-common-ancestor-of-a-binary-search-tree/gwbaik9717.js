// h : height of BST
// Time complexity: O(h)
// Space complexity: O(h)

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  if (root.val < p.val && root.val < q.val && root.left) {
    return lowestCommonAncestor(root.right, p, q);
  }

  if (root.val > p.val && root.val > q.val && root.right) {
    return lowestCommonAncestor(root.left, p, q);
  }

  return root;
};
