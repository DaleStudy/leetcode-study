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

// Approach 3:
// Time Complexity: O(n)
// Space Complexity: O(n), due to the recursion stack

function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;

  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}

// Approach 2:
// Time Complexity: O(n)
// Space Complexity: O(n)

// function maxDepth(root: TreeNode | null): number {
//   if (!root) return 0;

//   let maxDepth = 0;
//   let stack: Array<[TreeNode, number]> = [[root, 1]];

//   while (stack.length > 0) {
//     const item = stack.pop();

//     if (!item) continue;

//     const [node, depth] = item;

//     maxDepth = Math.max(maxDepth, depth);

//     if (node.left) {
//       stack.push([node.left, depth + 1]);
//     }

//     if (node.right) {
//       stack.push([node.right, depth + 1]);
//     }
//   }

//   return maxDepth;
// }


// Approach 1
// Time Compleixty:O(n)
// Space Complexity:O(n), due to the recursion stack

// function maxDepth(root: TreeNode | null): number {
//   let maxCnt = 0;

//   const dfs = (node: TreeNode | null, cnt: number) => {
//     if (!node) {
//       maxCnt = Math.max(maxCnt, cnt);
//       return;
//     }

//     dfs(node.left, cnt + 1);
//     dfs(node.right, cnt + 1);
//   };

//   dfs(root, 0);

//   return maxCnt;
// }

