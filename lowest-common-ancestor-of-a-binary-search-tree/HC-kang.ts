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

/**
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description
 * T.C. O(log n)
 * S.C. O(log n)
 */
function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode | null,
  q: TreeNode | null
): TreeNode | null {
  if (!root) return null;
  if (root.val > p!.val && root.val > q!.val) {
    return lowestCommonAncestor(root.left, p, q);
  } else if (root.val < p!.val && root.val < q!.val) {
    return lowestCommonAncestor(root.right, p, q);
  } else {
    return root;
  }
}

/**
 * iterative
 * T.C. O(log n)
 * S.C. O(1)
 */
function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode | null,
  q: TreeNode | null
): TreeNode | null {
  while (root) {
    if (root.val > p!.val && root.val > q!.val) {
      root = root.left;
    } else if (root.val < p!.val && root.val < q!.val) {
      root = root.right;
    } else {
      return root;
    }
  }
  return null;
}
