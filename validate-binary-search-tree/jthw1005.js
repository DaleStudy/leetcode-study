function isValidBST(root) {
  function helper(node, min, max) {
    if (!node) return true;
    if (node.val <= min || node.val >= max) return false;
    return (
      helper(node.left, min, node.val) && helper(node.right, node.val, max)
    );
  }
  return helper(root, -Infinity, Infinity);
}
