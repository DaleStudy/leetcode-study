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
  // 기본 케이스: 노드가 없는 경우 깊이는 0
  if (root === null) {
      return 0;
  }
  
  // 왼쪽 서브트리의 최대 깊이
  const leftDepth = maxDepth(root.left);
  
  // 오른쪽 서브트리의 최대 깊이
  const rightDepth = maxDepth(root.right);
  
  // 현재 노드의 깊이는 왼쪽과 오른쪽 서브트리 중 더 깊은 것에 1을 더한 값
  return Math.max(leftDepth, rightDepth) + 1;
}