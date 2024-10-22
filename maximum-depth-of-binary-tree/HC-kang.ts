// class TreeNode {
//   val: number;
//   left: TreeNode | null;
//   right: TreeNode | null;
//   constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//     this.val = val === undefined ? 0 : val;
//     this.left = left === undefined ? null : left;
//     this.right = right === undefined ? null : right;
//   }
// }

/**
 * https://leetcode.com/problems/maximum-depth-of-binary-tree
 * using recursion
 * T.C. O(n)
 * S.C. O(n)
 */
function maxDepth(root: TreeNode | null): number {
  return dfs(root, 0);
}

function dfs(node: TreeNode | null, depth: number): number {
  if (!node) {
    return depth;
  }
  return Math.max(dfs(node.left, depth + 1), dfs(node.right, depth + 1));
}

/**
 * using stack
 * T.C. O(n)
 * S.C. O(n)
 */
function maxDepth(root: TreeNode | null): number {
  if (!root) {
    return 0;
  }

  let max = 0;

  const stack: [TreeNode | null, number][] = [];
  stack.push([root, 1]);

  while (stack.length) {
    const [node, depth] = stack.pop()!;

    if (node) {
      max = Math.max(max, depth);
      stack.push([node.left, depth + 1]);
      stack.push([node.right, depth + 1]);
    }
  }

  return max;
}
