/*
230. Kth Smallest Element in a BST

Example 1:
    3
   / \
  1   4
   \
    2
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
        5
       / \
      3   6
     / \
    2   4
   /
  1
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 */

// class TreeNode {
//     val: number
//     left: TreeNode | null
//     right: TreeNode | null
//     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//         this.val = (val===undefined ? 0 : val)
//         this.left = (left===undefined ? null : left)
//         this.right = (right===undefined ? null : right)
//     }
// }

// Time complexity: O(n)
// Space complexity: O(n)
function kthSmallest(root: TreeNode | null, k: number): number {
  function inorder(root: TreeNode | null, arr: number[]) {
    if (!root) return;

    inorder(root.left, arr);
    arr.push(root.val);
    inorder(root.right, arr);
  }

  const arr: number[] = [];
  inorder(root, arr);
  return arr[k - 1];
}
