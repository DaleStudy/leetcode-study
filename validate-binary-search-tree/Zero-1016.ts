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
type Frame = {
  node: TreeNode | null;
  min: number;
  max: number;
};

/**
 * 반복적 DFS로 각 노드가 부모 노드가 정한 값 범위 (min, max) 안에 있는지 검사한다.
 * - 왼쪽 자식으로 내려가면 상한(max)이 현재 노드 값으로 좁아지고,
 * - 오른쪽 자식으로 내려가면 하한(min)이 현재 노드 값으로 좁아진다.
 *
 * 시간 복잡도: O(n) — 모든 노드를 한 번씩 방문
 * 공간 복잡도: O(n) — 최악의 경우 스택 크기 (평균적으로는 O(h))
 */
function isValidBST(root: TreeNode | null): boolean {
  const stack: Frame[] = [{ node: root, min: -Infinity, max: Infinity }];

  while (stack.length > 0) {
    const { node, min, max } = stack.pop()!;
    if (!node) continue;

    // NOTE 부모 노드들이 정한 범위를 벗어나면 유효한 BST가 아니다.
    if (node.val <= min || node.val >= max) return false;

    stack.push({ node: node.left, min, max: node.val });
    stack.push({ node: node.right, min: node.val, max });
  }

  return true;
}
