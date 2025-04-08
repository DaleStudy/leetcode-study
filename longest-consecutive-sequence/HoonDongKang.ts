/**
 * [Problem]: [128] Longest Consecutive Sequence
 * (https://leetcode.com/problems/longest-consecutive-sequence/description/)
 */

function longestConsecutive(nums: number[]): number {
  // 시간 복잡도 O(n)
  // 공간 복잡도 O(n)
  function sortFunc(nums: number[]): number {
    const setArr = new Set(nums);
    let longestCount = 0;

    for (let num of setArr) {
      if (!setArr.has(num - 1)) {
        let current = num;
        let count = 1;

        while (setArr.has(current + 1)) {
          current++;
          count++;
        }

        longestCount = Math.max(count, longestCount);
      }
    }
    return longestCount;
  }

  return sortFunc(nums);
}
