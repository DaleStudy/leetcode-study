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

/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(h), h는 트리의 높이 (최악의 경우 O(n))
 */
function isValidBST(root: TreeNode | null, min?: number, max?: number): boolean {
    if (root === null) return true;
    
    if (min !== undefined && root.val <= min) return false
    if (max !== undefined && root.val >= max) return false

    return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max)
};
