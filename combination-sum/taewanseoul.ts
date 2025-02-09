/**
 * 39. Combination Sum
 * Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
 * The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
 * The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
 *
 * https://leetcode.com/problems/combination-sum/description/
 */

// O(n^m) time
// O(n) space
function combinationSum(candidates: number[], target: number): number[][] {
  const res: number[][] = [];
  dfs(candidates, 0, target, [], res);
  return res;
}

function dfs(
  nums: number[],
  start: number,
  remaining: number,
  path: number[],
  res: number[][]
) {
  if (remaining === 0) {
    res.push([...path]);
    return;
  }

  for (let i = start; i < nums.length; i++) {
    const num = nums[i];
    if (remaining - num < 0) continue;
    path.push(num);
    dfs(nums, i, remaining - num, path, res);
    path.pop();
  }
}
