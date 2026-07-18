/**
 * @param {TreeNode} root
 * @return {boolean}
 */
// TC: O(n) / SC: Best O(height) - Worst O(n)
var isValidBST = function (root) {
  function traverse(node, min, max) {
    if (!node) return true;
    if (!(min < node.val && node.val < max)) return false;
    return traverse(node.left, min, node.val) && traverse(node.right, node.val, max);
  }

  return traverse(root, -Infinity, Infinity);
};
