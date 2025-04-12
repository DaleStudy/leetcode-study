/**
 * [Problem]: [217] Contains Duplicate
 * (https://leetcode.com/problems/contains-duplicate/description/)
 */

function containsDuplicate(nums: number[]): boolean {
  // 시간복잡도: O(n^2)
  // 공간복잡도: O(1)
  const doubleLoopFunc = (nums: number[]) => {
    let isDuplicated = false;
    for (let i = 0; i < nums.length; i++) {
      for (let j = i + 1; j < nums.length; j++) {
        if (nums[i] === nums[j]) isDuplicated = true;
      }
    }
    return isDuplicated;
  };

  // 시간복잡도: O(n)
  // 공간복잡도: O(n)
  const setFunc = (nums: number[]) => {
    const numsSet = new Set<number>(nums);

    return nums.length !== numsSet.size;
  };

  // 시간복잡도: O(n)
  // 공간복잡도: O(n)
  const mapFunc = (nums: number[]) => {
    const numsMap = new Map<number, boolean>();

    for (const num of nums) {
      if (numsMap.get(num)) return true;
      numsMap.set(num, true);
    }

    return false;
  };

  return mapFunc(nums);
}
