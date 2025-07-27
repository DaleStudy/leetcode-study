function containsDuplicate(nums: number[]): boolean {
  return new Set(nums).size !== nums.length;
}
/**
 * runtime: 24ms / Beats 27.12%
 * memory 74.42MB / Beats 55.98%
 */
