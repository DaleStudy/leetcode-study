/* 
시간 복잡도(TC): O(n)
공간 복잡도(SC): O(h) - h는 Tree의 높이
풀이: DFS를 활용하여, 각 노드의 값이 BST 조건을 만족하는지 확인한다. BST 조건은 왼쪽 서브트리의 모든 노드 값은 부모 노드 값보다 작아야 하고, 오른쪽 서브트리의 모든 노드 값은 부모 노드 값보다 커야 한다. 이를 위해 각 노드를 방문할 때마다 허용되는 최소값과 최대값을 갱신하며 재귀적으로 확인한다.
기타: 🟡자력 해결 실패. 추후 보충 학습 필요.
*/

class TreeNode {
  val: number
  left: TreeNode | null
  right: TreeNode | null
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val
    this.left = left === undefined ? null : left
    this.right = right === undefined ? null : right
  }
}

const dfs = (node: TreeNode | null, low: number, high: number): boolean => {
  if (!node) return true
  if (!(low < node.val && node.val < high)) return false
  return dfs(node.left, low, node.val) && dfs(node.right, node.val, high)
}

const isValidBST = (root: TreeNode | null): boolean => {
  return dfs(root, -Infinity, Infinity)
}
