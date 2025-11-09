/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  if (nums.length == 0) return 0;
  let answer = 0;
  let numsSet = new Set(nums);
  const N = nums.length;

  for (let num of numsSet) {
    if (!numsSet.has(num - 1)) {
      let temp = num;
      let length = 1;

      while (numsSet.has(temp + 1)) {
        length += 1;
        temp += 1;
      }
      // console.log(length)
      answer = Math.max(length, answer);
    }
  }

  return answer;
};
