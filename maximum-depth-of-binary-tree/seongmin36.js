/**
이 문제를 푸는 핵심은 DFS(깊이 우선 탐색)다.
왼쪽으로, 오른쪽으로 쭉 들어가는 값을 반환해서 변수에 저장한다.
이를 재귀호출하면 쉽게 해결할 수 있다.
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
function maxDepth(root) {
  if (root === null) return 0;

  let left_depth = maxDepth(root.left);
  let right_depth = maxDepth(root.right);

  let count = Math.max(left_depth, right_depth) + 1;

  return count;
}
