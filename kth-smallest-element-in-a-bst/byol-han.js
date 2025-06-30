/**
 * https://leetcode.com/problems/kth-smallest-element-in-a-bst/
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
  // 중위 순회 결과를 저장할 배열
  const inorder = [];

  // 중위 순회 함수 정의
  function traverse(node) {
    if (!node) return;
    traverse(node.left); // 왼쪽 서브트리 방문
    inorder.push(node.val); // 현재 노드 값 추가
    traverse(node.right); // 오른쪽 서브트리 방문
  }

  // 트리 순회 시작
  traverse(root);

  // k번째로 작은 값 반환 (1-indexed 이므로 k-1)
  return inorder[k - 1];
};
