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
 *
 * 접근 방법 :
 *  - DFS로 루트 노드를 찾은 뒤, 하위 트리가 동일한 트리인지 확인하기
 *
 * 시간복잡도 : O(n * m)
 *  - n = root 트리 노드의 개수
 *  - m = subRoot 트리 노드의 개수
 *  - 루트 노드 찾기 위해서 O(n)
 *  - 동일 트리 체크하기 위해서 O(m)
 *
 * 공간복잡도 : O(n + m)
 *  - n = root 트리 높이
 *  - m = subRoot 트리 높이
 *  - dfs 탐색 최대 깊이 O(n)
 *  - isSameTree 탐색 최대 깊이 O(m)
 *
 */
function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
  if (!root) return false;

  const isSameTree = (
    node: TreeNode | null,
    subNode: TreeNode | null
  ): boolean => {
    // 두 노드가 null이면 동일한 트리
    if (!node && !subNode) return true;
    // 한 노드만 null이면 다른 트리
    if (!node || !subNode) return false;
    // 값이 다르면 다른 트리
    if (node.val !== subNode.val) return false;

    // 값이 같으니까 왼쪽, 오른쪽 하위 트리도 비교
    return (
      isSameTree(node.left, subNode.left) &&
      isSameTree(node.right, subNode.right)
    );
  };

  // 루트 노드 찾기
  const dfs = (node: TreeNode | null): boolean => {
    if (!node) return false;
    // 동일한 트리인지 확인
    if (isSameTree(node, subRoot)) return true;
    // 왼쪽이나 오른쪽 추가 탐색 진행
    return dfs(node.left) || dfs(node.right);
  };

  return dfs(root);
}
