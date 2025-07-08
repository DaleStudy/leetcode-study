/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val === undefined ? 0 : val);
 *     this.left = (left === undefined ? null : left);
 *     this.right = (right === undefined ? null : right);
 * }
 */

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    const res = [];
    if (!root) return res;

    const q = [root];

    while (q.length > 0) {
        const qLen = q.length;
        const level = [];

        for (let i = 0; i < qLen; i++) {
            const node = q.shift();
            if (node) {
                level.push(node.val);
                if (node.left) q.push(node.left);
                if (node.right) q.push(node.right);
            }
        }

        if (level.length > 0) {
            res.push(level);
        }
    }

    return res;
};

