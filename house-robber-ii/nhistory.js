var rob = function (nums) {
  // edge case
  if (nums.length === 1) return nums[0];

  const dp = (start, end) => {
    let prev = 0,
      curr = 0;
    for (let i = start; i < end; i++) {
      let temp = curr;
      curr = Math.max(nums[i] + prev, curr);
      prev = temp;
    }
    return curr;
  };

  return Math.max(dp(0, nums.length - 1), dp(1, nums.length));
};

// TC: O(n)
// SC: O(1)
