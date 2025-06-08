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
 * @return {TreeNode}
 */
var invertTree = function (root) {
  if (!root) return null;

  const queue = [root];

  while (queue.length > 0) {
    const current = queue.shift();

    // 자식 노드들 바꾸기
    [current.left, current.right] = [current.right, current.left];

    // 자식 노드들을 큐에 추가
    if (current.left) queue.push(current.left);
    if (current.right) queue.push(current.right);
  }

  return root;
};
