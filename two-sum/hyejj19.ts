function twoSum(nums: number[], target: number): number[] {
  for (let lt = 0; lt < nums.length - 1; lt++) {
    for (let rt = lt + 1; rt < nums.length; rt++) {
      if (nums[lt] + nums[rt] === target) return [lt, rt];
    }
  }
  return [0, 0];
}
