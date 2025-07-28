function twoSum(nums: number[], target: number): number[] {
  const visited: { [key: string]: boolean } = {};
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (visited[complement]) {
      const complementIdx = nums.indexOf(complement);
      return [i, complementIdx];
    }
    visited[nums[i]] = true;
  }
  return [];
}

/**
 * runtime: O(n)
 * memory O(n)
 */
