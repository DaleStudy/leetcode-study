/**
 * @description
 * 최대 깊이를 탐색하는 문제여서 dfs를 먼저 떠올렸지만 이번에 bfs로 풀이하고 싶어 bfs로 풀었습니다.
 *
 * n = total node count
 * time complexity: O(n)
 * space complexity: O(n)
 */
var maxDepth = function (root) {
  const queue = [];
  let lastIndex = queue.length;
  let answer = 0;

  if (!root) return answer;

  queue.push(root);

  while (queue.length !== lastIndex) {
    let currentCount = queue.length - lastIndex;
    answer++;

    while (currentCount--) {
      let currentNode = queue[lastIndex];
      lastIndex++;
      if (currentNode.left) queue.push(currentNode.left);
      if (currentNode.right) queue.push(currentNode.right);
    }
  }

  return answer;
};
