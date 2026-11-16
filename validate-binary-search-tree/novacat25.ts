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
  if (!node) return true // Null인 Node는 BST 조건을 만족한다고 간주해 재귀적으로 True를 반환한다.
  if (!(low < node.val && node.val < high)) return false // 현재 Node의 값이 허용 범위에 속하지 않으면 False를 반환한다.
  return dfs(node.left, low, node.val) && dfs(node.right, node.val, high) // 왼쪽 서브트리와 오른쪽 서브트리를 재귀적으로 확인하며, 허용 범위를 갱신한다.
}

const isValidBST = (root: TreeNode | null): boolean => {
  return dfs(root, -Infinity, Infinity) // 초기 허용 범위를 -Infinity와 Infinity로 설정하여 Root Node부터 시작한다.
}
