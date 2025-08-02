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

function isValidBST(root: TreeNode | null): boolean {
  const queue: [TreeNode, number, number][] = [[root, -Infinity, +Infinity]];

  while (queue.length > 0) {
    const [currentNode, minVal, maxVal] = queue.shift();

    if (minVal >= currentNode.val || currentNode.val >= maxVal) return false;

    if (currentNode.left) {
      queue.push([currentNode.left, minVal, currentNode.val]);
    }
    if (currentNode.right) {
      queue.push([currentNode.right, currentNode.val, maxVal]);
    }
  }

  return true;
}
