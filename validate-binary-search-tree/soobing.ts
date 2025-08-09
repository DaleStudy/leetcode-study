/**
 * 문제 유형
 * - Tree
 *
 * 문제 설명
 * - 이진 탐색 트리가 맞는지 확인하기
 *
 * 아이디어
 * 1) 중위 순회 후 정렬된 배열인지 확인
 *
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

function isSorted(arr: number[]) {
  for (let i = 1; i < arr.length; i++) {
    if (arr[i - 1] >= arr[i]) return false;
  }
  return true;
}
function inorder(node: TreeNode | null, arr: number[]) {
  if (node === null) return;
  inorder(node.left, arr);
  arr.push(node.val);
  inorder(node.right, arr);
}
function isValidBST(root: TreeNode | null): boolean {
  const sortedArray: number[] = [];
  inorder(root, sortedArray);
  return isSorted(sortedArray);
}
