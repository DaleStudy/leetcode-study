function twoSum(nums: number[], target: number): number[] {
  const table = new Map();
  nums.forEach((num, idx) => table.set(num, idx));

  for (let i = 0; i < nums.length; i++) {
    const result = target - nums[i];
    if (table.has(result) && table.get(result) !== i) {
      return [i, table.get(result)];
    }
  }
}
