/**
 * 이진 트리를 반전시키는 함수
 * @param {TreeNode | null} root - 반전할 이진 트리의 루트 노드
 * @returns {TreeNode | null} - 반전된 이진 트리의 루트 노드
 * 
 * 시간 복잡도: O(n) 
 *  - 트리의 모든 노드를 한 번씩 방문해야 하므로 선형 시간 복잡도를 가짐
 * 공간 복잡도: O(h) 
 * - 재귀 호출에 의해 최대 트리의 높이(h)만큼의 호출 스택이 필요
 */
function invertTree(root: TreeNode | null): TreeNode | null {
  // 루트가 null이면 null 반환
  if (!root) return null;

  // 왼쪽과 오른쪽 서브트리를 재귀적으로 반전
  const left = invertTree(root.left);
  const right = invertTree(root.right);

  // 현재 노드의 왼쪽과 오른쪽 서브트리를 교환
  root.left = right;
  root.right = left;

  // 반전된 루트 노드를 반환
  return root;
}

