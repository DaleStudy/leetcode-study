/**
 * 시간복잡도 O(n^(T/m))
 * 풀이방법: DFS 백트래킹
 * 결과: 2ms
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
const combinationSum = function (candidates, target) {
  const result = [];
  const nums = [];

  const sortedCandidates = candidates.sort((a, b) => a - b);

  function dfs(start, sum) {
    if (sum === target) {
      result.push([...nums]);
    }

    for (let i = start; i < sortedCandidates.length; i += 1) {
      const num = sortedCandidates[i];

      if (sum + num > target) break;

      nums.push(num);
      dfs(i, sum + num);
      nums.pop();
    }
  }

  dfs(0, 0);

  return result;
};
