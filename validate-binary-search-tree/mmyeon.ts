/**
 *
 * 접근 방법 :
 *  - 이진 탐색 트리의 특징(왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드)을 이용하여 문제 풀기
 *  - 부모 노드 값, 최상위 루트 노드 값을 모두 고려해야 하니까 min, max로 값의 범위 지정하기
 *
 * 시간복잡도 : O(n)
 *  - n = root 트리 노드의 개수
 *  - 모든 노드 탐색 : O(n)
 *
 * 공간복잡도 : O(h)
 *  - h = root 트리 높이
 *  - 재귀 호출이 트리 높이만큼 발생함
 *  - 치우친 트리의 경우 h = O(n)
 *
 */
function isValidBST(root: TreeNode | null): boolean {
  function helper(node: TreeNode | null, min: number, max: number): boolean {
    if (!node) return true;

    if (node.val <= min || node.val >= max) return false;

    return (
      helper(node.left, min, node.val) && helper(node.right, node.val, max)
    );
  }

  return helper(root, -Infinity, Infinity);
}
