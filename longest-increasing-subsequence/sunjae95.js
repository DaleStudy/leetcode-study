/**
 * @description
 * brainstorming:
 * 1. dfs -> time limited
 * 2. memoization + dfs
 *
 * n: length of nums
 * time complexity: O(n^2)
 * space complexity: O(n)
 */
var lengthOfLIS = function (nums) {
  const memo = new Array(nums.length).fill(-1);
  let answer = 0;

  const dfs = (index) => {
    if (memo[index] !== -1) return memo[index];

    let maxLength = 1;

    for (let i = index + 1; i < nums.length; i++) {
      if (nums[index] < nums[i]) {
        maxLength = Math.max(maxLength, 1 + dfs(i));
      }
    }

    memo[index] = maxLength;
    return maxLength;
  };

  for (let i = 0; i < nums.length; i++) {
    answer = Math.max(answer, dfs(i));
  }

  return answer;
};
