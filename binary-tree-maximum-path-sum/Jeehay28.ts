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

// TC: O(n)
// SC: O(n)
function maxPathSum(root: TreeNode | null): number {
  let maxSum = -Infinity;

  const dfs = (node: TreeNode | null) => {
    if (!node) return 0;

    const leftMax = Math.max(dfs(node.left), 0);
    const rightMax = Math.max(dfs(node.right), 0);

    maxSum = Math.max(node.val + leftMax + rightMax, maxSum);

    return node.val + Math.max(leftMax, rightMax);
  };

  dfs(root);
  return maxSum;
}
