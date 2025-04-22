// 시간복잡도: O(n) 모든 노드를 한번씩 방문하기 때문에 n
// 공간복잡도: O(n) 최악의 경우 모든 노드가 한줄로 이어져 있을 때 스택에 모든 노드를 저장해야 하기 때문에 n

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
var maxDepth = function (root) {
  if (!root) return 0;
  
  return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
};

console.log(maxDepth([3, 9, 20, null, null, 15, 7]));
console.log(maxDepth([1, null, 2]));