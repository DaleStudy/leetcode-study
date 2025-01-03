// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const n = nums.length;
  const fromLeft = Array.from({ length: n + 1 }, () => 1);
  const fromRight = Array.from({ length: n + 1 }, () => 1);

  for (let i = 1; i <= n; i++) {
    fromLeft[i] = fromLeft[i - 1] * nums[i - 1];
  }

  for (let i = n - 1; i >= 0; i--) {
    fromRight[i] = fromRight[i + 1] * nums[i];
  }

  return nums.map((num, i) => {
    return fromLeft[i] * fromRight[i + 1];
  });
};
