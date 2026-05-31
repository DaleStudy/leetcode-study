class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function isValidBST(root: TreeNode | null): boolean {
  function valid(node, min, max) {
    if (!node) return true;

    if (node.val <= min || node.val >= max) return false;

    return valid(node.left, min, node.val) && valid(node.right, node.val, max);
  }

  return valid(root, -Infinity, Infinity);
}
