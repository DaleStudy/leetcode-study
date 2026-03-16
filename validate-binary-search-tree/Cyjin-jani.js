const isValidBST = function (root) {
  let answer = true;

  function validateRecursion(node, min, max) {
    if (!node) return;

    if (node.val >= max || node.val <= min) {
      answer = false;
      return;
    }
    if (node.val <= min || node.val >= max) {
      answer = false;
      return;
    }

    validateRecursion(node.left, min, node.val);
    validateRecursion(node.right, node.val, max);
  }

  validateRecursion(root, -Infinity, Infinity);

  return answer;
};
