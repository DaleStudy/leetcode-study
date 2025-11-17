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

// Time Complexity: O(k) - 최악의 경우 모든 노드를 방문하면 O(n)
// Space Complexity: O(h) - 재귀 호출 스택의 최대 깊이 (h는 트리의 높이)
function kthSmallest(root: TreeNode | null, k: number): number {
  let count = 0;
  let result = 0;

  const inorder = (node: TreeNode | null): void => {
    if (!node) return;

    inorder(node.left);

    count++;
    if (count === k) {
      result = node.val;
      return;
    }

    inorder(node.right);
  };

  inorder(root);

  return result;
}
