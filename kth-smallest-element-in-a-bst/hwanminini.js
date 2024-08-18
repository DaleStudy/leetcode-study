// 시간 복잡도: O(n log n)
// 공간 복잡도: O(n)

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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    const results = []

    const dfs = (tree) => {
        results.push(tree.val)
        if (tree.left) dfs(tree.left)
        if (tree.right) dfs(tree.right)
    }

    dfs(root)

    results.sort((a,b) => a - b)

    return results[k-1]
};
