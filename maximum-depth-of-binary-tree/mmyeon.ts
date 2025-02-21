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
 * @link https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
 *
 * 접근 방법 : DFS 사용
 *  - 각 노드에서 왼쪽 서브트리와 오른쪽 서브트리 깊이 계산한 후, 더 깊은 값에 1 더하기
 *  - 종료 조건 : 노드가 null일 때 0 반환
 *
 * 시간복잡도 : O(n)
 *  - n = 트리의 노드 개수
 *  - 노드 한 번씩 방문해서 깊이 계산
 *
 * 공간복잡도 : O(n)
 *  - 기울어진 트리의 경우, 트리 최대 깊이만큼 재귀 호출 스택 쌓임
 */
function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;

  return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
}
