/**
 * @param {number[]} nums
 * @return {number}
 */
const longestConsecutive = (nums) => {
  if (nums.length === 0) return 0;

  const numSet = new Set(nums);
  let maxLength = 0;

  for (const num of numSet) {
    // 시퀀스 시작점만 체크
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let currentLength = 1;

      // 연속된 숫자 카운트
      while (numSet.has(currentNum + 1)) {
        currentNum++;
        currentLength++;
      }

      maxLength = Math.max(maxLength, currentLength);
    }
  }

  return maxLength;
};
