/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

// Rumtime: 0ms
// Memory: 54.38MB

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    
    if(!p || !q) {
    return p === q;
    }

  return p.val === q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)

};
