/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  const memo = new Map();
  return dfs(nums, 0, memo);
};

const dfs = (nums, i, memo) => {
  if (i >= nums.length) return 0;
  if (memo.has(i)) return memo.get(i);
  const result = Math.max(
    nums[i] + dfs(nums, i + 2, memo),
    dfs(nums, i + 1, memo),
  );
  memo.set(i, result);
  return result;
};
