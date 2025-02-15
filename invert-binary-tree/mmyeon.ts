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
 * @link https://leetcode.com/problems/invert-binary-tree/description/
 *
 * 접근 방법 : 깊이 우선 탐색(DFS) 사용
 * - 각 노드의 좌우 자식 노드 swap 진행
 * - 왼쪽, 오른쪽 서브트리에 대해 재귀적으로 호출
 *
 * 시간복잡도 : O(n)
 *  - n은 노드의 개수, 주어진 노드 만큼 순회
 *
 * 공간복잡도 : O(h)
 *  - h : 트리의 높이
 *  - 호출 스택 최대 트리 높이만큼 쌓임
 */
function invertTree(root: TreeNode | null): TreeNode | null {
  if (!root) return root;

  [root.left, root.right] = [root.right, root.left];
  invertTree(root.left);
  invertTree(root.right);

  return root;
}

/**
 *
 * 접근 방법 : 너비 우선 탐색(BFS) 사용
 * - root 노드를 큐에 담고, 큐가 빌 때까지 좌우 자식 노드 swap과 큐에 추가 하는 로직 반복하기
 *
 * 시간복잡도 : O(n)
 * - n: 트리 노드의 개수
 * - 모든 노드를 한 번 씩 방문하고 swap 작업 진행
 *
 * 공간복잡도 : O(n)
 *  - 최악의 경우 치우친 트리인 경우 모든 노드 순차적으로 큐에 저장
 */
function invertTree(root: TreeNode | null): TreeNode | null {
  if (!root) return root;

  const queue = [root];

  while (queue.length) {
    const node = queue.shift()!;

    [node.left, node.right] = [node.right, node.left];

    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }

  return root;
}
