/**
 * 문제 설명
 * - 이진 탐색 트리의 두 노드의 최소 공통 조상을 찾는 문제
 *
 * 아이디어
 * 1) 두 노드의 값을 비교하여 최소 공통 조상을 찾는다.
 *   - 두 노드의 값이 루트 노드보다 작으면 왼쪽 서브트리로 이동
 *   - 두 노드의 값이 루트 노드보다 크면 오른쪽 서브트리로 이동
 *   - 두 노드의 값이 루트 노드와 같으면 루트 노드를 반환
 *
 */

function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode | null,
  q: TreeNode | null
): TreeNode | null {
  if (root === null) return null;
  if (p === null || q === null) return null;

  while (root !== null) {
    if (p.val < root.val && q.val < root.val) {
      root = root.left;
    } else if (p.val > root.val && q.val > root.val) {
      root = root.right;
    } else {
      return root;
    }
  }

  return root;
}
