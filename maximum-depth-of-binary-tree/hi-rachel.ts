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

// O(n) time, 모든 노드를 한 번씩 방문
// O(h) for DFS / O(w) for BFS space, DFS는 재귀 호출 깊이 (h = 트리 높이), BFS는 큐에 들어가는 최대 노드 수 (w = 최대 너비)

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

// BFS 풀이
function maxDepth(root: TreeNode | null): number {
  if (root === null) return 0;

  const queue: TreeNode[] = [root];
  let depth = 0;

  while (queue.length > 0) {
    const levelSize = queue.length;

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      if (node) {
        if (node.left) queue.push(node.left);
        if (node.right) queue.push(node.right);
      }
    }
    depth++;
  }
  return depth;
}

// DFS 풀이
// function maxDepth(root: TreeNode | null): number {
//   if (root === null) return 0;
//   const left = maxDepth(root.left);
//   const right = maxDepth(root.right);
//   return Math.max(left, right) + 1;
// }
