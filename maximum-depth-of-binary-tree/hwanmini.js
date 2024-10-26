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
 * @return {number}
 */
var maxDepth = function(root) {
    if (!root) return 0;

    let maxDepth = 0;
    const exploreMaxDepth = (node, depth) => {
        if (!node) {
            maxDepth = Math.max(maxDepth, depth)
            return
        }


        exploreMaxDepth(node.left, depth + 1)
        exploreMaxDepth(node.right, depth + 1)
    }

    exploreMaxDepth(root, 0)

    return maxDepth
};
