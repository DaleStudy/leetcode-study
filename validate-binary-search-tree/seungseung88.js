/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
  let prev = -Infinity;

  const inorder = (node) => {
    if (!node) return true;

    if (!inorder(node.left)) return false;

    if (node.val <= prev) return false;
    prev = node.val;

    return inorder(node.right);
  };

  return inorder(root);
};
