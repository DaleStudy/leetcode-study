function containsDuplicate(nums: number[]): boolean {
  const sets = new Set<number>(nums);
  return sets.size < nums.length;
}
