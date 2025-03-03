/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
    const left = Math.min(p.val, q.val);
    const right = Math.max(p.val, q.val);

    const dfs = (node) => {
        if (!node) {
            return;
        }

        if (node.val >= left && node.val <= right) {
            return node;
        }

        if (node.val > left && node.val > right) {
            return dfs(node.left);
        }

        if (node.val < left && node.val < right) {
            return dfs(node.right);
        }
    }
    
    return dfs(root);
};

// 시간복잡도 O(logn) -> 이진트리를 이진탐색하면서 트리의 노드를 방문하기떄문(동일한 깊이에서 한 번 왼쪽을 방문하였다면, 그 깊이에서 오른쪽을 방문하지 않음)
// 공간복잡도 O(h) -> 재귀호출을 사용하였으므로 트리의 높이만큼 최대 콜스택의 쌓임이 발생

