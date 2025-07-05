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
const levelOrder = function(root) {
    if (!root) return [];
    
    const queue = [[root]];
    const result = [];

    while (queue.length) {
        const curNodes = queue.shift();
        const newNodes = []; // 나중에 queue에 넣을 배열로 child node들이 들어감
        const newResult = []; // 나중에 result에 넣을 배열로 node.val이 들어감

        curNodes.forEach((node) => {
            newResult.push(node.val);
            if (node.left) newNodes.push(node.left);
            if (node.right) newNodes.push(node.right);
        });

        if (newNodes.length) queue.push(newNodes);
        result.push(newResult)
    }

    return result;
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)

/*
위 풀이는 배열을 4개 사용하고 있음
아래 풀이는 배열을 줄인 방식
*/
const levelOrder = function(root) {
    if (!root) return [];

    const queue = [root];
    const result = [];

    while (queue.length) {
        const level = [];
      
        // queue에 있는 노드 다 꺼내기
        for (let i = 0; i < queue.length; i++) {
            const node = queue.shift();
            level.push(node.val);

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        result.push(level);
    }

    return result;
};
