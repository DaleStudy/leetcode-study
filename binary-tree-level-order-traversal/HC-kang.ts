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
 * https://leetcode.com/problems/binary-tree-level-order-traversal
 * T.C. O(n)
 * S.C. O(n)
 */
function levelOrder(root: TreeNode | null): number[][] {
  const result: number[][] = [];
  function dfs(node: TreeNode | null, level: number) {
    if (!node) return;
    if (!result[level]) result[level] = [];
    result[level].push(node.val);
    dfs(node.left, level + 1);
    dfs(node.right, level + 1);
  }
  dfs(root, 0);
  return result;
}

/**
 * bfs
 * T.C. O(n)
 * S.C. O(n)
 */
function levelOrder(root: TreeNode | null): number[][] {
  const result: number[][] = [];
  if (!root) return result;

  const queue: TreeNode[] = [root];
  let start = 0;

  while (queue[start]) {
    const levelSize = queue.length - start;
    const currentLevel: number[] = [];

    for (let i = 0; i < levelSize; i++) {
      const node = queue[start++];
      currentLevel.push(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(currentLevel);
  }

  return result;
}
