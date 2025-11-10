function containsDuplicate(nums: number[]): boolean {
  const duplicateSet = new Set(nums);
  return duplicateSet.size !== nums.length;
}
