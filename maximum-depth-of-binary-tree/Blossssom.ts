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

/**
 * @param root - 이진 트리
 * @returns - 루트 노드에서 가장 먼 리프노드 까지 가장 긴 경로를 따른 노드 수
 * @description
 * - root가 없는 경우를 제외 후 재귀 호출로 1씩 증가
 * - left, right 중 가장 큰 값을 return
 * - maxDepth 자체를 재귀로 사용하는 방식이 가장 효율적
 */

// function maxDepth(root: TreeNode | null): number {
//   if (!root) {
//     return 0;
//   }

//   function recursive(current: TreeNode | null): number {
//     if (!current) {
//       return 0;
//     }

//     return 1 + Math.max(recursive(current.left), recursive(current.right));
//   }

//   return recursive(root);
// }

function maxDepth(root: TreeNode | null): number {
  if (root === null) {
    return 0;
  }

  const left = 1 + maxDepth(root.left);
  const right = 1 + maxDepth(root.right);

  return Math.max(left, right);
}

const root = new TreeNode(
  3,
  new TreeNode(9),
  new TreeNode(20, new TreeNode(15), new TreeNode(7))
);

