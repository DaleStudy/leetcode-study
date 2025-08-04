/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * 주어진 이진 트리의 최대 깊이를 반환하는 함수
 * @param {TreeNode} root
 * @return {number}
 */
const maxDepth = function(root) {
    let maxDepth = 0;

    function bfs(node, depth) {
        if (!node) return;
        
        depth += 1;
        if (maxDepth < depth) maxDepth = depth;
        bfs(node.left, depth);
        bfs(node.right, depth);
    }

    bfs(root, maxDepth);
    return maxDepth;
};

// 시간복잡도: O(n)
// 공간복잡도: O(h) (h: 트리의 높이. 최악의 경우 편향트리일 때 h===n으로 O(n))
