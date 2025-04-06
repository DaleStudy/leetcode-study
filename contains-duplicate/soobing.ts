function containsDuplicate(nums: number[]): boolean {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (map.get(nums[i])) {
      return true;
    } else map.set(nums[i], 1);
  }

  return false;
}
