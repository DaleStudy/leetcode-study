/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  if (nums.length === 0) return 0;

  const numSet = new Set(nums);
  let longest = 0;
  for (let num of numSet) {
    // `num - 1`이 없으면 새로운 수열의 시작점
    if (!numSet.has(num - 1)) {
      let count = 1;
      let currentNum = num;

      // 연속된 숫자 찾기
      while (numSet.has(currentNum + 1)) {
        currentNum++;
        count++;
      }

      longest = Math.max(longest, count);
    }
  }

  return longest;
};
