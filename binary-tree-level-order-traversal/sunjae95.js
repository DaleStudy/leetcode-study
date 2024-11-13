/**
 * @description
 * 동일한 depth를 방문해야하므로 bfs 및 트리 순회
 *
 * n = length of node of root
 * time complexity: O(n)
 * space complexity: O(n)
 */
var levelOrder = function (root) {
  if (!root) return [];

  const answer = [];
  const queue = [root];
  let queueCurrentIndex = 0;

  while (queue.length > queueCurrentIndex) {
    answer.push([]);
    const answerLastIndex = answer.length - 1;
    const depthEndIndex = queue.length;

    while (depthEndIndex !== queueCurrentIndex) {
      const tree = queue[queueCurrentIndex++];

      answer[answerLastIndex].push(tree.val);
      if (tree.left) queue.push(tree.left);
      if (tree.right) queue.push(tree.right);
    }
  }

  return answer;
};
