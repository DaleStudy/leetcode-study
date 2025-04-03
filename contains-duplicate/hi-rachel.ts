/**
 * 어떤 value든 array에서 2번 나오면 true 반환
 * 다 unique한 값이면 false 반환
 * O(N) time, O(N) space
 * */

function containsDuplicate(nums: number[]): boolean {
  let numMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (numMap.has(nums[i])) {
      return true;
    } else {
      numMap.set(nums[i], 1);
    }
  }
  return false;
}
