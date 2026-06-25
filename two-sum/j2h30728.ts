/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * @description
 * - 시간 복잡도: O(n^2)
 * - 공간 복잡도: O(1)
 */
function twoSum(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length - 1; i++) {
    const num = nums[i];
    const index = nums
      .slice(i + 1)
      .findIndex((vlaue) => vlaue === target - num);
    if (index > -1) {
      return [i, index + i + 1];
    }
  }
}

/**
 *
 * @param nums
 * @param target
 * @return {number[]}
 * @description
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 */
function twoSum(nums: number[], target: number): number[] {
  const map = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    const foundIndex = map.get(diff);

    if (foundIndex !== undefined) {
      return [foundIndex, i];
    }

    map.set(nums[i], i);
  }
  return [];
}
