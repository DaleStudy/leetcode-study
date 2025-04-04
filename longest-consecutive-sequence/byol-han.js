/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  if (nums.length === 0) return nums.length;

  const setNums = new Set(nums);
  const sortNums = [...setNums].sort((a, b) => a - b);

  let longest = 1;
  let currentlength = 1;

  for (let i = 0; i < sortNums.length; i++) {
    if (sortNums[i] + 1 === sortNums[i + 1]) {
      currentlength++;
      longest = Math.max(longest, currentlength);
    } else {
      currentlength = 1;
    }
  }
  return longest;
};
