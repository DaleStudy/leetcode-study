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
    const dfs = (node, min, max) => {
        if (!node) return true;
        if (!((node.val > min) && (node.val < max))) return false;

        return dfs(node.left, min, node.val) && dfs(node.right, node.val, max);
    }

    return dfs(root, Number.MIN_SAFE_INTEGER, Number.MAX_SAFE_INTEGER);
};

// 시간 복잡도 O(n) , 공간 복잡도 최악의 경우 O(n)
