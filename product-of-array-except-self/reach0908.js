/**
 * @description
 * time complexity: O(n)
 * space complexity: O(n)
 * runtime: 5ms
 * 풀이 방법 : 40분고민하다가 다른사람 풀이보고 누적합을 이용하면 된다해서 구현함
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const result = new Array(nums.length).fill(1);

  let prefix = 1;

  for (let i = 0; i < nums.length; i += 1) {
    result[i] = prefix;
    prefix *= nums[i];
  }

  let postfix = 1;

  for (let i = nums.length - 1; i >= 0; i -= 1) {
    result[i] *= postfix;
    postfix *= nums[i];
  }

  return result;
};
