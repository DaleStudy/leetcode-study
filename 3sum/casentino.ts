function threeSum(nums: number[]): number[][] {
  const sortedNums = nums.sort((a, b) => a - b);
  const results: number[][] = [];
  for (let i = 0; i < sortedNums.length - 2; i++) {
    const current = sortedNums[i];
    if (current > 0) {
      return results;
    }
    if (i > 0 && current === sortedNums[i - 1]) {
      continue;
    }
    let left = i + 1;
    let right = sortedNums.length - 1;
    while (left < right) {
      const sum = current + sortedNums[left] + sortedNums[right];
      if (sum > 0) {
        right -= 1;
      } else if (sum < 0) {
        left += 1;
      } else {
        results.push([current, sortedNums[left], sortedNums[right]]);
        left += 1;
        right -= 1;
        while (left < right && sortedNums[left] === sortedNums[left - 1]) {
          left += 1;
        }
        while (left < right && sortedNums[right] === sortedNums[right + 1]) {
          right -= 1;
        }
      }
    }
  }
  return results;
}
