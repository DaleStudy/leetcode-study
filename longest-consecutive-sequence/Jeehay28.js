/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  let result = [];
  let longest = [];

  numsSorted = nums.sort((a, b) => a - b);

  numsFiltered = [...new Set(numsSorted)];

  for (let i = 0; i < numsFiltered.length; i++) {
    if (result.length === 0) {
      result.push(numsFiltered[i]);
    } else if (result.length >= 1) {
      if (numsFiltered[i] === result[result.length - 1] + 1) {
        result.push(numsFiltered[i]);
      } else {
        longest.push(result.length);
        result = [numsFiltered[i]];
      }
    }
  }

  if (longest.length === 0) {
    return result.length;
  } else {
    return Math.max(Math.max(...longest), result.length);
  }
};
