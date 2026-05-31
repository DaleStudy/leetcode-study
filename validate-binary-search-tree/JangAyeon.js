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
const dfs = (node, left, right) => {
  if (!node) {
    return true;
  }

  return (
    node.val > left &&
    node.val < right &&
    dfs(node.left, left, node.val) &&
    dfs(node.right, node.val, right)
  );
};

const isValidBST = function (root) {
  return dfs(root, -Infinity, Infinity);
};
