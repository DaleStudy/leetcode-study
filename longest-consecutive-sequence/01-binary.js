/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const unique_arr = Array.from(new Set(nums));
  const temp = unique_arr.sort((a, b) => a - b);
  let a = 1;
  let max = 0;
  for (let i = 0; i < temp.length; i++) {
    if (temp[i] + 1 === temp[i + 1]) {
      a++;
    } else {
      max = Math.max(a, max);
      a = 1;
    }
  }
  return max;
};
