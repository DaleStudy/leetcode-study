function twoSum(nums: number[], target: number): number[] {
  const numsLen = nums.length;
  const result: number[] = [];

  for (let i = 0; i < numsLen - 1; i++) {
    for (let j = i + 1; j < numsLen; j++) {
      if (nums[i] + nums[j] === target) {
        result.push(i);
        result.push(j);
        break;
      }
    }
  }

  return result;
}
