function threeSum(nums: number[]): number[][] {
  let result: [number, number, number][] = [];
  const TARGET = 0;
  // TC: O(NlogN)
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      let sum = nums[i] + nums[left] + nums[right];

      if (sum === TARGET) {
        result.push([nums[i], nums[left], nums[right]]);
        while (nums[left] === nums[left + 1]) left++;
        while (nums[right] === nums[right - 1]) right--;
        left++;
        right--;
      } else if (sum < TARGET) {
        left++;
      } else {
        right--;
      }
    }
  }

  return result;
}
// TC: O(n^2)
// SC: O(n)
