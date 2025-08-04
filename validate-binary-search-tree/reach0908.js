/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root, low = -Infinity, high = Infinity) {
  if (!root) {
    return true;
  }

  if (root.val <= low || root.val >= high) {
    return false;
  }

  return (
    isValidBST(root.left, low, root.val) &&
    isValidBST(root.right, root.val, high)
  );
};
