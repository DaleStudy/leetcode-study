function threeSum(nums: number[]): number[][] {
  // Sort the array to make it easier to find triplets that sum to zero
  nums.sort((a, b) => a - b);
  const result: number[][] = [];

  // Iterate through the array to find triplets that sum to zero
  for (let i = 0; i < nums.length - 2; i++) {
    // Skip duplicates
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    // Use two pointers to find the other two numbers
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) {
        // Add the triplet to the result array
        result.push([nums[i], nums[left], nums[right]]);
        left++;
        right--;
        // Skip duplicates
        while (left < right && nums[left] === nums[left - 1]) left++;
        while (left < right && nums[right] === nums[right + 1]) right--;
      } else if (sum < 0) {
        // Move the left pointer to the right to increase the sum
        left++;
      } else {
        // Move the right pointer to the left to decrease the sum
        right--;
      }
    }
  }

  return result;
}
