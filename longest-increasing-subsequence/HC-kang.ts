/**
 * https://leetcode.com/problems/longest-increasing-subsequence
 * T.C. O(nlogn)
 * S.C. O(n)
 */
function lengthOfLIS(nums: number[]): number {
  const sub: number[] = [];

  function findSlot(num: number): number {
    let left = 0;
    let right = sub.length - 1;

    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      if (sub[mid] < num) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    return left;
  }

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const slot = findSlot(num);
    sub[slot] = num;
  }

  return sub.length;
}
