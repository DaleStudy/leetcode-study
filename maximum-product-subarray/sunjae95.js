/**
 * @description
 * brainstorming:
 * 1. memoization, recursive
 * 2. palindromic-substring custom
 */

/**
 * brainstorming solve 1
 * result: fail because time limited
 *
 * time complexity: O(n^2)
 * space complexity: O(n^2)
 */
var maxProduct = function (nums) {
  let answer = nums[0];

  const memo = Array.from({ length: nums.length }, () =>
    Array.from({ length: nums.length }, () => null)
  );

  const recursive = (left, right) => {
    if (memo[left][right] !== null) return memo[left][right];

    if (left === right) {
      memo[left][right] = nums[left];
      answer = Math.max(answer, nums[left]);
      return nums[left];
    }

    const removedLeft = recursive(left + 1, right);
    recursive(left, right - 1);

    memo[left][right] = nums[left] * removedLeft;

    answer = Math.max(answer, memo[left][right]);

    return removedLeft;
  };

  recursive(0, nums.length - 1);

  return answer;
};

/**
 * brainstorming solve 2
 * result: fail because time limited
 *
 * time complexity: O(n^2)
 * space complexity: O(n)
 */
var maxProduct = function (nums) {
  let answer = nums[0];

  for (let i = 0; i < nums.length; i++) {
    let [start, end] = [i, i];
    let product = nums[i];

    answer = Math.max(answer, product);
    while (start >= 0 && end < nums.length) {
      if (start !== end) product = product * nums[start] * nums[end];

      answer = Math.max(answer, product);
      [start, end] = [start - 1, end + 1];
    }

    product = nums[i];
    [start, end] = [i, i + 1];

    while (start >= 0 && end < nums.length) {
      if (start + 1 === end) product = product * nums[end];
      else product = product * nums[start] * nums[end];

      answer = Math.max(answer, product);
      [start, end] = [start - 1, end + 1];
    }
  }

  return answer;
};
