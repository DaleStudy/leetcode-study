/**
 * Time Complexity: O(n) (using a single pass with a hash map)
 * (If a nested loop was used, it would be O(n^2))
 */
function twoSum(nums: number[], target: number): number[] {
  const numAndIndex = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];

    if (numAndIndex.has(diff)) {
      return [numAndIndex.get(diff)!, i];
    }

    numAndIndex.set(nums[i], i);
  }

  return [];
}
