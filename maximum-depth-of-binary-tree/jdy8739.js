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
var maxDepth = function (root) {
    let max = 0;

    const dfs = (node, depth) => {
        if (node) {
            dfs(node.left, depth + 1);
            dfs(node.right, depth + 1);
        } else { // when this node is null
            max = Math.max(max, depth);
        }
    }

    dfs(root, 0);

    return max;
};

// 시간복잡도 O(n) -> 트리의 모든 노드를 방문하면서 총 노드의 갯수인 n개 만큼의 시간복잡도를 가지게 되므로
// 공간복잡도 O(h) -> 콜스택의 최대 길이는 트리의 깊이와 동일하므로

