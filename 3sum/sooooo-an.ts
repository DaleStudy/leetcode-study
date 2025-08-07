function threeSum(nums: number[]): number[][] {
  nums.sort((a: number, b: number) => a - b);
  const results: [number, number, number][] = [];

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const current = nums[i] + nums[left] + nums[right];
      if (current === 0) {
        results.push([nums[i], nums[left], nums[right]]);

        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;

        left++;
        right--;
      } else if (current < 0) {
        left++;
      } else if (current > 0) {
        right--;
      }
    }
  }

  return results;
}
