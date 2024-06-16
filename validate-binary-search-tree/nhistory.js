var isValidBST = function (root) {
  return validate(root, -Infinity, Infinity);
};

function validate(node, min, max) {
  if (!node) return true; // An empty tree is a valid BST
  if (node.val <= min || node.val >= max) return false; // Current node's value must be between min and max

  // Recursively validate the left and right subtree
  return (
    validate(node.left, min, node.val) && validate(node.right, node.val, max)
  );
}
