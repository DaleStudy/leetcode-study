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
 * https://leetcode.com/problems/binary-tree-maximum-path-sum
 * T.C. O(n)
 * S.C. O(n)
 */
function maxPathSum(root: TreeNode | null): number {
  let max = -Infinity;

  function dfs(node: TreeNode | null): number {
    if (!node) return 0;

    const left = Math.max(0, dfs(node.left));
    const right = Math.max(0, dfs(node.right));

    max = Math.max(max, node.val + left + right);

    return node.val + Math.max(left, right);
  }

  dfs(root);

  return max;
}

/**
 * iterative using stack
 * T.C. O(n)
 * S.C. O(n)
 */
function maxPathSum(root: TreeNode | null): number {
  let max = -Infinity;
  const stack: Array<TreeNode | null> = [root];
  const memo = new Map<TreeNode, number>();

  while (stack.length) {
    const node = stack.pop();

    if (!node) continue;

    if (memo.has(node)) {
      const left = Math.max(0, node.left ? memo.get(node.left)! : 0);
      const right = Math.max(0, node.right ? memo.get(node.right)! : 0);

      max = Math.max(max, node.val + left + right);

      memo.set(node, node.val + Math.max(left, right));
    } else {
      stack.push(node, node.right, node.left);
      memo.set(node, 0);
    }
  }

  return max;
}
