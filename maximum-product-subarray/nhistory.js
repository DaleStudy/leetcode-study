var maxProduct = function (nums) {
  let result = nums[0];
  let max = 1,
    min = 1;

  for (const num of nums) {
    const candidates = [min * num, max * num, num];
    min = Math.min(...candidates);
    max = Math.max(...candidates);
    result = Math.max(max, result);
  }
  return result;
};

// TC: O(n)
// SC: O(1)
