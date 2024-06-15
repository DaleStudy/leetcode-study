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
function isValidBST(root, low = -Infinity, high = Infinity) {
  if (root === null) {
    return true;
  }

  if (root.val <= low || root.val >= high) {
    return false;
  }

  return (
    // left root should be less than current root
    isValidBST(root.left, low, root.val) &&
    // right root should be greater than current root
    isValidBST(root.right, root.val, high)
  );
}
