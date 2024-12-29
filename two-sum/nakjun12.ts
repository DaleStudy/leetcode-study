/*
 * TC: O(n)
 * SC: O(n)
 * */
function twoSum(nums: number[], target: number): number[] {
  const indices = {};

  for (let i = 0; i < nums.length; i++) {
    const curNum = nums[i];
    const complement = target - curNum;

    if (complement in indices) {
      return [indices[complement], i];
    }

    indices[curNum] = i;
  }

  return [];
}
