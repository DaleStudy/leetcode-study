function threeSum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b);

  const result: number[][] = [];
  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    const target = -nums[i];

    let j = i + 1;
    let k = nums.length - 1;
    while (j < k) {
      const currentSum = nums[j] + nums[k];

      if (target < currentSum) {
        k--;
      } else if (target > currentSum) {
        j++;
      } else {
        result.push([nums[i], nums[j], nums[k]]);

        j++;
        k--;

        while (j < k && nums[j] === nums[j - 1]) j++;
        while (j < k && nums[k] === nums[k + 1]) k--;
      }
    }
  }

  return result;
}
