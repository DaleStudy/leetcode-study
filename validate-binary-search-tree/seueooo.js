/**
중위 순회하면서 계속 값이 커지는지 확인
시간복잡도 O(n)
공간복잡도 O(n)
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
  let prev = -Infinity;

  const inOrder = (node) => {
    if (!node) return true;
    if (!inOrder(node.left)) return false;
    if (node.val <= prev) return false;
    prev = node.val;
    return inOrder(node.right);
  };
  return inOrder(root);
};
