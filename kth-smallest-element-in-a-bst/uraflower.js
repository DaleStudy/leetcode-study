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
const kthSmallest = function (root, k) {
    const sorted = [];

    const traverse = function (root) {
        if (!root) return;
        traverse(root.left);
        sorted.push(root.val);
        traverse(root.right);
    }

    traverse(root);
    return sorted[k - 1];
};

// 시간복잡도: O(n)
// 공간복잡도: O(n) (배열)
