/**
 * @description
 * brainstorming:
 * dfs
 *
 * time complexity: O(n^k)
 * space complexity: O(n)
 */
var combinationSum = function (candidates, target) {
  const answer = [];

  const dfs = (array, sum, index) => {
    if (sum > target) return;
    if (sum === target) return answer.push(array);

    for (let i = index; i < candidates.length; i++) {
      const nextArray = array.concat(candidates[i]);
      const nextSum = sum + candidates[i];

      dfs(nextArray, nextSum, i);
    }
  };

  candidates.forEach((value, i) => dfs([value], value, i));

  return answer;
};
