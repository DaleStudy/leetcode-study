function twoSum(nums: number[], target: number): number[] {
  const table = new Map();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (table.has(complement)) {
      return [table.get(complement)!, i];
    }

    table.set(nums[i], i);
  }

  return [];
}
