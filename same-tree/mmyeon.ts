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
 *@link https://leetcode.com/problems/same-tree/description/
 *
 * 접근 방법 :
 *  - 두 노드의 값이 같을 때, 좌우 하위 트리를 재귀적으로 비교하기
 *
 * 시간복잡도 : O(n)
 *  - n = 트리 노드 개수
 *  - 모든 노드를 한 번씩 방문한다.
 *
 * 공간복잡도 : O(n)
 *  - 최악의 경우(기울어진 트리), 트리 높이만큼 재귀가 호출 된다.
 */
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
  if (p === null && q === null) return true;

  // false 조건 : 둘 중 하나만 null일 때, 두 노드의 값이 다른 경우
  if (p === null || q === null || p.val !== q.val) return false;

  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
