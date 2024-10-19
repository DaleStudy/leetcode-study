// 시간복잡도: O(n)
// 공간복잡도: O(n)

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (!root) return null;

    const left = root.left
    const right = root.right

    root.left = right
    root.right = left


    invertTree(left)
    invertTree(right)

    return root
};