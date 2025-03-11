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
 * @return {number[][]}
 */
var levelOrder = function (root) {
    if (!root) {
        return [];
    }

    const queue = [root];
    const answer = [];

    while (queue.length > 0) {
        const values = [];

        const currentQueueLen = queue.length;

        for (let i = 0; i < currentQueueLen; i++) {
            const head = queue.shift();

            values.push(head.val);

            head.left && queue.push(head.left);
            head.right && queue.push(head.right);
        }

        answer.push(values);
    }

    return answer;
};

// 시간복잡도 O(n) -> 모든 노드를 한번씩 너비우선탐색으로 방문하므로
// 공간복잡도 O(n) -> 큐에 모든 노드의 값을 저장하므로
