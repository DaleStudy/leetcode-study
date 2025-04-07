/**
 * Finds two numbers in the array that add up to the target value.
 * Uses a hash map to store previously seen numbers for O(n) time complexity.
 *
 * @param nums - An array of integers.
 * @param target - The target sum.
 * @returns A tuple containing the indices of the two numbers.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
function twoSum(nums: number[], target: number): number[] {
  const map = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
      const complement = target - nums[i];
      if (map.has(complement)) {
          return [map.get(complement)!, i];
      }
      map.set(nums[i], i);
  }

  throw new Error("No solution found");
}
