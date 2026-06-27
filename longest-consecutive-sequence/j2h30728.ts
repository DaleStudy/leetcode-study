/**
 *
 * @param nums
 * @returns
 * 시간 복잡도 : O(n log n)
 * 공간 복잡도 : O(n)
 */
function longestConsecutive(nums: number[]): number {
  if (nums.length === 0) {
    return 0;
  }

  const set = new Set(nums);
  const arr = [...set].sort((a, b) => a - b);
  let count = 1;
  let max = 1;

  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i + 1] - arr[i] === 1) {
      count += 1;
    } else {
      max = Math.max(count, max);
      count = 1;
    }
  }
  return Math.max(max, count);
}

/**
 *
 * @param nums
 * @returns
 * 시간 복잡도 : O(n)
 * 공간 복잡도 : O(n)
 */
function longestConsecutive(nums: number[]): number {
  const set = new Set(nums);
  let max = 0;

  for (let num of set) {
    if (!set.has(num - 1)) {
      let current = num;
      let count = 1;

      while (set.has(current + 1)) {
        count++;
        current++;
      }
      max = Math.max(count, max);
    }
  }

  return max;
}
