/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let answer = [];

  const p = [];
  for (let i = 0; i < nums.length; i++) {
    if (i == 0) {
      const n = nums.slice(i + 1).reduce((acc, curr) => (acc *= curr), 1);
      console.log(n);
      p.push([1, n]);
      answer.push(1 * n);
    } else {
      const [left, right] = p[i - 1];
      if (nums[i] === 0) {
        const n = nums.slice(i + 1).reduce((acc, curr) => (acc *= curr), 1);
        p.push([left * nums[i - 1], n]);
        answer.push(left * nums[i - 1] * n);
      } else {
        p.push([left * nums[i - 1], right / nums[i]]);
        answer.push((left * nums[i - 1] * right) / nums[i]);
      }
    }
  }

  return answer;
};
