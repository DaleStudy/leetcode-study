function twoSum(nums: number[], target: number): number[] {
  const sz = nums.length;
  let l = 0,
    r = 1,
    sm = nums[0] + nums[1];

  while (l <= sz - 2 && r <= sz - 1) {
    sm = nums[l] + nums[r];

    if (sm === target) {
      return [l, r];
    }

    if (l === r - 1) {
      (r++, (l = 0));
    } else {
      l++;
    }
  }
}
