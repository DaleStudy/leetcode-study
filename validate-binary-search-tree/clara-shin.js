/**
 * 이진탐색트리 유효성 검사 (Valid Binary Search Tree) 확인하는 함수 만들기
 * 검사할 조건 3가지
 * 1. 왼쪽 서브트리의 모든 노드 값은 루트 노드 값보다 작아야 한다.
 * 2. 오른쪽 서브트리의 모든 노드 값은 루트 노드 값보다 커야 한다.
 * 3. 왼쪽 서브트리와 오른쪽 서브트리도 각각 이진탐색트리여야 한다.
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 * val: 노드가 저장하는 값입니다.
 * left: 왼쪽 자식 노드를 가리키는 참조
 * right: 오른쪽 자식 노드를 가리키는 참조
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
  const searchBST = (node, min, max) => {
    if (node === null) return true;
    if (node.val <= min || node.val >= max) return false;
    return searchBST(node.left, min, node.val) && searchBST(node.right, node.val, max);
  };

  return searchBST(root, -Infinity, Infinity);
};
