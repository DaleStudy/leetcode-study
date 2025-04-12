class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

function isValidBST(root: TreeNode | null): boolean {
  // Helper function to check if a tree is a valid binary search tree
  function isValidTree(node: TreeNode | null, min: number | null, max: number | null): boolean {
    // If the node is null, the tree is valid
    if (node === null) return true;

    // If the node's value is less than the minimum or greater than the maximum, the tree is not valid
    if ((min !== null && node.val <= min) || (max !== null && node.val >= max)) {
      return false;
    }

    // Recursively check the left and right subtrees
    return isValidTree(node.left, min, node.val) && isValidTree(node.right, node.val, max);
  }

  // Check if the tree is a valid binary search tree
  return isValidTree(root, null, null);
}
