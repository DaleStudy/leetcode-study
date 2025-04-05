// 1번째 풀이 (brute force)
function twoSum1(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 1; j < nums.length; j++) {
      const a = nums[i];
      const b = nums[j];

      if (a + b === target && i !== j) {
        return [i, j];
      }
    }
  }
  return [];
};

// 2번째 풀이 (indexOf)
function twoSum2(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length; i++) {
    const j = target - nums[i];
    const index = nums.indexOf(j);

    if (index !== -1 && i !== index) {
      return [i, index];
    }
  }
  return [];
};

// 3번째 풀이 (HashMap)
function twoSum3(nums: number[], target: number): number[] {
  const map: Record<number, number> = {};

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (complement in map) {
      const j = map[complement];
      return [i, j];
    } else {
      map[nums[i]] = i;
    }
  }

  return [];
};
