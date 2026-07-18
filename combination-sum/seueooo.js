/*
백트래킹, dfs
시간복잡도 O(N^(T / M))
공간복잡도 O(T / M)

N = candidates.length
T = target
M = candidates 중 최솟값

 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  let result = [];

  function dfs(start, path, sum) {
    if (sum === target) {
      result.push([...path]);
      return;
    }
    if (sum > target) return;

    for (let i = start; i < candidates.length; i++) {
      path.push(candidates[i]);
      dfs(i, path, sum + candidates[i]);
      path.pop();
    }
  }

  dfs(0, [], 0);

  return result;
};
