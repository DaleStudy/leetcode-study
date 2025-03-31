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
var maxPathSum = function(root) {
    let max = root.val;

    const dfs = (node) => {
        if (!node) {
            return 0;
        }

        const left = Math.max(dfs(node.left), 0);
        const right = Math.max(dfs(node.right), 0);
        const sum = node.val + left + right;

        max = Math.max(sum, max);

        return node.val + Math.max(left, right);
    }

    dfs(root);

    return max;
};

// 시간복잡도 O(n) -> 트리의 모든 노드를 재귀적으로 탐색하므로 복잡도는 노드의 수와 비례함
// 공간복잡도 O(h) -> 입력된 트리의 최대 높이만큼 재귀 스택이 쌓이므로 공간복잡도는 트리의 높이와 같음
