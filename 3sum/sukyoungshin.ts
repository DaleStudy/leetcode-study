function threeSum(nums: number[]): number[][] {
  nums.sort((a, b) => a - b);
  const result: number[][] = [];
  const target = 0;

  for (let i = 0; i < nums.length - 2; i++) {
    // 중복된 시작 숫자는 건너뛰기
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum === target) {
        result.push([nums[i], nums[left], nums[right]]);

        // 중복된 left 값 건너뛰기
        while (left < right && nums[left] === nums[left + 1]) left++;
        // 중복된 right 값 건너뛰기
        while (left < right && nums[right] === nums[right - 1]) right--;

        // 다음 조합 시도
        left++;
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }

  return result;
};
