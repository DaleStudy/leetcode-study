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
var invertTree = function (root) {
    const dfs = (node) => {
        if (!node) {
            return null;
        }

        const temp = node.left;
        node.left = node.right;
        node.right = temp;

        dfs(node.left);
        dfs(node.right);
    }

    dfs(root);

    return root;
};

// 시간복잡도 O(n) 깊이우선탐색으로 모든 노드를 순회하므로 
