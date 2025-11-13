/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  let result = 1;
  let maxLength = 1;

  if (nums.length === 0) return 0;

  const sortedNums = nums.sort((a, b) => a - b);

  for (let i = 1; i < sortedNums.length; i++) {
    const prevNum = sortedNums[i - 1];
    const currentNum = sortedNums[i];

    const diff = currentNum - prevNum;

    if (diff === 1) {
      result += 1;

      if (maxLength < result) {
        maxLength = result;
      }
    } else if (diff === 0) {
      continue;
    } else {
      result = 1;
    }
  }

  return maxLength;
};
