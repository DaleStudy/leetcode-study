// Approach 2
// 🗓️ 2025-04-11
// ⏳ Time Complexity: O(n)
// 💾 Space Complexity: O(h) → O(log n) for balanced, O(n) for skewed trees

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

function isValidBST(root: TreeNode | null): boolean {
  // 🟡 중위 순회 (Inorder Traversal)
  // 방문 순서: 왼쪽 자식 → 현재 노드 → 오른쪽 자식

  let maxVal = -Infinity;

  const dfs = (node: TreeNode | null) => {
    if (!node) return true;

    if (!dfs(node.left)) return false;

    if (node.val <= maxVal) return false;

    maxVal = node.val;

    if (!dfs(node.right)) return false;

    return true;
  };

  return dfs(root);
}

// Approach 1
// 🗓️ 2025-04-11
// ⏳ Time Complexity: O(n)
// 💾 Space Complexity: O(h) → O(log n) for balanced, O(n) for skewed trees

// function isValidBST(root: TreeNode | null): boolean {
//   // 좌측 서브 트리로 내려갈 때:
//   // 하한값: 부모 노드 하한값
//   // 상한값: 부모 노드 값
//   // 우측 서브 트리로 내려갈 때:
//   // 우측 하한값: 부모 노드 값
//   // 우측 상한값: 부모 노드의 상한 값
//   // 🟢 전위 순회 (Preorder Traversal)
//   // 방문 순서: 현재 노드 → 왼쪽 자식 → 오른쪽 자식

//   const dfs = (node: TreeNode | null, low: number, high: number) => {
//     if (!node) return true;

//     if (!(node.val > low && node.val < high)) return false;

//     return dfs(node.left, low, node.val) && dfs(node.right, node.val, high);
//   };

//   return dfs(root, -Infinity, Infinity);
// }
