/**
 * @description
 * memoization + dfs
 *
 * n = length of nums
 * p = length of prerequisites
 *
 * time complexity: O(n)
 * space complexity: O(p)
 */
var canFinish = function (numCourses, prerequisites) {
  const memo = Array.from({ length: numCourses + 1 }, () => false);
  const visited = Array.from({ length: numCourses + 1 }, () => false);
  // graph setting
  const graph = prerequisites.reduce((map, [linkedNode, current]) => {
    const list = map.get(current) ?? [];
    list.push(linkedNode);
    map.set(current, list);
    return map;
  }, new Map());

  const dfs = (current) => {
    const linkedNode = graph.get(current);

    if (memo[current] || !linkedNode || linkedNode.length === 0) return true;

    for (const node of linkedNode) {
      if (visited[node]) return false;

      visited[node] = true;
      if (!dfs(node)) return false;
      visited[node] = false;
      memo[node] = true;
    }

    return true;
  };

  for (const [current] of graph) {
    visited[current] = true;
    if (!dfs(current)) return false;
    visited[current] = false;
    memo[current] = true;
  }

  return true;
};
