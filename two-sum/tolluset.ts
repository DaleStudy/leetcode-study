/*
 * TC: O(n)
 * SC: O(n)
 * */
function twoSum(nums: number[], target: number): number[] {
  const n = nums.length;
  const answer = new Map<number, number>();

  for (let i = 0; i < n; i++) {
    const diff = target - nums[i];
    const before = answer.get(diff);

    if (before) {
      return [before, i];
    }

    answer.set(nums[i], i);
  }

  return [];
}
