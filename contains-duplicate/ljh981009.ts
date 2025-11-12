function containsDuplicate(nums: number[]): boolean {
  const result = new Set(nums);
  return result.size !== nums.length;
}
