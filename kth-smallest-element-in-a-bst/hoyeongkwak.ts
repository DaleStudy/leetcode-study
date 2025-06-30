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
/*
Time Complexity: O(h + k)
Space Complexity: O(h)
*/
function kthSmallest(root: TreeNode | null, k: number): number {
    let count = 0
    let result = -1
    const inOrder = (node: TreeNode | null): void => {
        if (node == null || count >= k) return

        inOrder(node.left)
        count++
        if (count === k) {
            result = node.val
            return
        }
        inOrder(node.right)
    }
    inOrder(root)
    return result
};
