function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {
  if (!root) {
    return null;
  }

  const originLeft = root.left;
  const originRight = root.right;

  root.right = invertTree(originLeft);
  root.left = invertTree(originRight);

  return root;
};
