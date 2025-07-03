/**
 * 문제 설명
 * - 이진 탐색 트리(BST)가 주어졌을 때, k번째 작은 요소를 찾는 문제
 *
 * 아이디어
 * 1) 중위 순회를 하면서 k번째 작은 요소를 찾는다.
 *  - 이진 탐색 트리(BST)는 중위 순회(in-order traversal)하면 오름차순으로 정렬된 값을 얻을 수 있다.
 */

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function kthSmallest(root: TreeNode | null, k: number): number {
  let result = -1;
  let count = 0;

  function inOrder(node: TreeNode | null) {
    if (!node || result !== -1) return;

    inOrder(node.left);
    count++;

    if (count === k) {
      result = node.val;
      return;
    }

    inOrder(node.right);
  }

  inOrder(root);
  return result;
}
