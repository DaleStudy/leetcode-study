function containsDuplicate(nums: number[]): boolean {
  return nums.length !== new Set(nums).size;
}
