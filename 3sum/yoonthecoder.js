var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  const results = [];
  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1;
    let right = nums.length - 1;
    while (left < right) {
      const currSum = nums[i] + nums[left] + nums[right];

      if (currSum == 0) {
        results.push([nums[i], nums[left], nums[right]]);
        left++;
        right--;
        // to avoid duplicates
        while (left < right && nums[left] === nums[left - 1]) left++;
        while (left < right && nums[right] === nums[right + 1]) right--;
      } else if (currSum < 0) {
        left++;
      } else right--;
    }
  }
  return results;
};

// Time complexity: O(n^2);
// Space complexity: O(n)
