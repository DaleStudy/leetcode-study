/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val);
 *     this.left = (left===undefined ? null : left);
 *     this.right = (right===undefined ? null : right);
 * }
 */

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function(root) {
    let res = [root.val];

    function dfs(node) {
        if (!node) return 0;

        let leftMax = dfs(node.left);
        let rightMax = dfs(node.right);

        leftMax = Math.max(leftMax, 0);
        rightMax = Math.max(rightMax, 0);

        // 경유지점 포함한 경로 최대값 업데이트
        res[0] = Math.max(res[0], node.val + leftMax + rightMax);

        // 분기하지 않는 경로에서의 최대값 리턴
        return node.val + Math.max(leftMax, rightMax);
    }

    dfs(root);
    return res[0];
};

