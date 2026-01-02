/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
 
function maxDepth(root: TreeNode | null): number {
  // DFS (혹은 BFS) 후 깊이 체크하기
  if (!root) return 0;
  
  const stack: [TreeNode, number][] = [[root, 1]];
  let maxDepth = 0;

  while (stack.length > 0) {
    const [node, depth] = stack.pop()!;
    maxDepth = Math.max(maxDepth, depth);

    if (node.right) {
      stack.push([node.right, depth + 1]);
    }
    if (node.left) {
      stack.push([node.left, depth + 1]);
    }
  }

  return maxDepth;
};
