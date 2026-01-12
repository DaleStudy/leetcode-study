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
 * @param root - TreeNode 객체
 * @returns - 좌우 반전된 root 반환
 * @description
 * - 모든 트리를 탐색하기 위해 bfs로 진행
 * - queue 배열을 만들어 각 단계의 하위 left, right를 push
 */

function invertTree(root: TreeNode | null): TreeNode | null {
  if (root === null) {
    return null;
  }

  const queue = [root];

  while (queue.length) {
    const current = queue.shift()!;

    [current.left, current.right] = [current.right, current.left];

    if (current.left !== null) {
      queue.push(current.left);
    }

    if (current.right !== null) {
      queue.push(current.right);
    }
  }

  return root;
}

const root = new TreeNode(
  4,
  new TreeNode(2, new TreeNode(1), new TreeNode(3)),
  new TreeNode(7, new TreeNode(6), new TreeNode(9))
);

invertTree(root);



