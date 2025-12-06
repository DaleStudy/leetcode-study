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
 * @return {number}
 */
var maxDepth = function(root) {
    if(!root) return 0

    const dfs = (node, level) =>{
        if(!node) return level;

        let left = level;
        let right = level

        if(node.left){
            left = dfs(node.left, level+1)
        }

        if(node.right){
            right = dfs(node.right, level+1)
        }

        return Math.max(left,right);
    }

    return dfs(root,1)
};
