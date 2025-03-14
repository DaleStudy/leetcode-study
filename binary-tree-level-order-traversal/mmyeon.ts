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
 *@link https://leetcode.com/problems/binary-tree-level-order-traversal/
 *
 * 접근 방법 : DFS 사용
 *  - 같은 높이의 노드들을 result 배열에 넣기 위해서 dfs로 재귀 호출
 *  - result 배열에 현재 level에 대한 배열이 없으면 추가하고, 현재 노드의 값을 push
 *  - 하위 자식 노드가 존재하면 dfs 재귀 호출 (level은 1 증가)
 *
 * 시간복잡도 : O(n)
 *  - n = 노드의 개수, 모든 노드 순회
 *
 * 공간복잡도 : O(n)
 *  - 트리 기울어진 경우, 재귀 호출 n번 만큼 스택 사용
 */

function levelOrder(root: TreeNode | null): number[][] {
  const result: number[][] = [];

  const dfs = (node: TreeNode | null, level: number) => {
    if (!node) return;

    if (!result[level]) result[level] = [];

    result[level].push(node.val);

    if (node.left) dfs(node.left, level + 1);
    if (node.right) dfs(node.right, level + 1);
  };

  dfs(root, 0);

  return result;
}

/**
 *
 * 접근 방법 : BFS 사용
 *  - 동일 레벨의 노드 값 담기 위해서 큐를 사용
 *  - 탐색할 노드를 큐에 먼저 담고, 큐에서 하나씩 꺼내면서 동일 레벨의 노드 값 담기
 *  - 노드의 자식노드가 존재하면 다시 큐에 추가해서 탐색할 수 있도록 함
 *  - 이 과정 반복하기
 *
 * 시간복잡도 : O(n)
 *  - n = 노드의 개수, 모든 노드 순회
 *
 * 공간복잡도 : O(n)
 *  - 큐에 모든 노드 저장함
 */

function levelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];

  // 탐색할 노드 담아놓는 대기줄
  const queue: TreeNode[] = [root];
  const result: number[][] = [];

  while (queue.length > 0) {
    // 동일 레벨에 있는 노드 값 담는 용도
    const currentLevel: number[] = [];
    // queue 사이즈가 동적으로 변하기 때문에 미리 계산한 값 변수에 저장
    const size = queue.length;

    for (let i = 0; i < size; i++) {
      const node = queue.shift()!;
      currentLevel.push(node.val);

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    result.push(currentLevel);
  }

  return result;
}
