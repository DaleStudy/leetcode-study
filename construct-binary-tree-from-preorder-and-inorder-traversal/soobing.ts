/**
 * 문제 설명
 * - preorder(전위순회), inorder(중위순회) 배열을 통해 이진트리를 복원한다
 *
 *
 * 아이디어
 * 1) preorder 배열의 요소는 루트 노드이다, 이를 기준으로 inorder 배열을 좌우로 나눈다.
 * 2) 좌우로 나눈 inorder 배열의 길이를 통해 preorder 배열의 좌우 서브트리를 구한다.
 * 3) 이를 재귀적으로 반복한다.
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

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  if (preorder.length === 0 || inorder.length === 0) return null;

  const inorderIndexMap = new Map<number, number>();
  inorder.forEach((value, index) => inorderIndexMap.set(value, index));

  let preorderIndex = 0;
  const helper = (left: number, right: number): TreeNode | null => {
    if (left > right) return null;
    const rootValue = preorder[preorderIndex++];
    const root = new TreeNode(rootValue);
    const index = inorderIndexMap.get(rootValue)!;

    root.left = helper(left, index - 1);
    root.right = helper(index + 1, right);

    return root;
  };

  return helper(0, inorder.length - 1);
}
