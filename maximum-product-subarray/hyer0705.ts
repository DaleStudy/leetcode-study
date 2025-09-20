function maxProduct(nums: number[]): number {
  let minValue = nums[0];
  let maxValue = nums[0];
  let result = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const currentNum = nums[i];
    [minValue, maxValue] = [
      Math.min(currentNum, maxValue * currentNum, minValue * currentNum),
      Math.max(currentNum, maxValue * currentNum, minValue * currentNum),
    ];

    result = Math.max(result, maxValue);
  }

  return result;
}
