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
/**
 * 트리의 깊이 구하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 * @param root
 */
function maxDepth(root: TreeNode | null): number {
  if(!root) return 0;
  let max = 0;
  let stack: [TreeNode | null, number][] = [[root, 1]];
  while(stack.length > 0) {
    const [node, depth] = stack.pop();
    max = Math.max(depth, max);
    if (node.left) stack.push([node.left, depth + 1]);
    if (node.right) stack.push([node.right, depth + 1]);
  }
  return max
}
