/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  if (nums.length == 0) return 0;
  let answer = 0;
  let numsSet = new Set(nums);
  const N = nums.length;

  for (let i = 0; i < N; i++) {
    let temp = nums[i];
    let length = 1;
    if (!numsSet.has(temp - 1)) {
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
