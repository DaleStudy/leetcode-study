/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  if (nums.length === 0) {
    return 0;
  }
  const set = new Set(nums);
  const uniquiArr = [...set];
  uniquiArr.sort((a, b) => a - b);
  const lengthArr = [1];
  for (let i = 1; i < uniquiArr.length; i++) {
    if (uniquiArr[i - 1] + 1 === uniquiArr[i]) {
      const last = lengthArr[lengthArr.length - 1] + 1;
      lengthArr.pop();
      lengthArr.push(last);
    } else {
      lengthArr.push(1);
    }
  }
  return Math.max.apply(null, lengthArr);
};
