/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (arr, target) {
  const N = arr.length;
  const answer = [];
  function dfs(total, idx, route) {
    if (total >= target) {
      if (total == target) {
        answer.push(route);
      }
      return;
    }
    for (let i = idx; i < N; i++) {
      dfs(total + arr[i], i, [...route, arr[i]]);
    }
  }

  dfs(0, 0, []);
  return answer;
};
