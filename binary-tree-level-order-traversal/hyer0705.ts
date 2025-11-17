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

// ----- [Solution 1]
// Time Complexity: O(n)
// Space Complexity: O(n)
function levelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const answer: number[][] = [];

  const queue: [TreeNode, number][] = [];
  let pointer = 0;

  queue.push([root, 0]);

  while (pointer < queue.length) {
    const [currNode, level] = queue[pointer++];

    if (!answer[level]) answer[level] = [];

    answer[level].push(currNode.val);

    if (currNode.left) queue.push([currNode.left, level + 1]);
    if (currNode.right) queue.push([currNode.right, level + 1]);
  }

  return answer;
}

// ----- [Solution 2]
// Time Complexity: O(n)
// Space Complexity: O(n)
function levelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  const answer: number[][] = [];

  const queue: TreeNode[] = [];
  queue.push(root);

  let pointer = 0;

  while (pointer < queue.length) {
    const levelSize = queue.length - pointer;
    const currentLevel: number[] = [];

    for (let i = 0; i < levelSize; i++) {
      const currNode = queue[pointer++];
      currentLevel.push(currNode.val);

      if (currNode.left) queue.push(currNode.left);
      if (currNode.right) queue.push(currNode.right);
    }

    answer.push(currentLevel);
  }

  return answer;
}
