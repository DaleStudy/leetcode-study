function isValidBST(root: TreeNode | null): boolean {
  return validateBSTHelper(root, -Infinity, Infinity);
}

const validateBSTHelper = (
  root: TreeNode | null,
  minValue: number,
  maxValue: number
): boolean => {
  if (root === null) {
    return true;
  }
  if (root.val <= minValue || root.val >= maxValue) {
    return false;
  }
  const leftIsValid = validateBSTHelper(root.left, minValue, root.val);
  return leftIsValid && validateBSTHelper(root.right, root.val, maxValue);
};
