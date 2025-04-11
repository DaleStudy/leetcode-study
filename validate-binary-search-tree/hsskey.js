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
 * @return {boolean}
 */
var isValidBST = function(root) {
    const dfs = (node, left = null, right = null) => {
        if(!node) {
            return true
        }

        if((left !== null && node.val <= left) || (right !== null && node.val >= right)) {
            return false
        }

        return dfs(node.left, left, node.val) && dfs(node.right, node.val, right)
    }

    return dfs(root)
};
