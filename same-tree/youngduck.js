/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  // 트리 순회 -> 재귀, 큐, 스택 방식들이 있음.
  //    두개의 트리를 동시에 조회하는 풀이

  // 둘 다 null이면 같음
  if (p === null && q === null) return true;

  // 하나만 null이면 다름
  if (p === null || q === null) return false;

  // 값이 다르면 다름
  if (p.val !== q.val) return false;

  // 왼쪽 자식들과 오른쪽 자식들이 모두 같아야 함
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

// 시간복잡도 O(N)
// 공간복잡도 O(N)
