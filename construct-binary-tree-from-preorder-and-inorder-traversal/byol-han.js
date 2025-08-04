/**
 * https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
  // 해시맵을 만들어 중위 순회의 값 -> 인덱스를 빠르게 찾을 수 있도록 함
  const inorderMap = new Map();
  inorder.forEach((val, idx) => {
    inorderMap.set(val, idx);
  });

  // preorder를 순회할 인덱스
  let preorderIndex = 0;

  /**
   * 재귀 함수: 현재 서브트리의 중위 순회 구간(start ~ end)을 기반으로 트리를 만든다.
   */
  function arrayToTree(left, right) {
    // 종료 조건: 구간이 잘못되면 노드가 없음
    if (left > right) return null;

    // preorder에서 현재 루트 값 선택
    const rootVal = preorder[preorderIndex];
    preorderIndex++; // 다음 호출을 위해 인덱스 증가

    // 현재 노드 생성
    const root = new TreeNode(rootVal);

    // 루트 값의 중위 순회 인덱스 찾기
    const index = inorderMap.get(rootVal);

    // 왼쪽 서브트리와 오른쪽 서브트리를 재귀적으로 생성
    root.left = arrayToTree(left, index - 1);
    root.right = arrayToTree(index + 1, right);

    return root;
  }

  // 전체 inorder 범위로 시작
  return arrayToTree(0, inorder.length - 1);
};
