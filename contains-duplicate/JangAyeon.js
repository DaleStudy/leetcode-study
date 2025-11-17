/**
 * @param {number[]} nums
 * @return {boolean}
 */

// 첫번째 제출
var containsDuplicate = function (nums) {
  const counter = new Map();
  for (let e of nums) {
    const v = counter.has(e) ? counter.get(e) + 1 : 1;
    counter.set(e, v);
  }
  const answer = [...counter.values()].some((item) => item >= 2);
  return answer;
};
// 두번째 제출
var containsDuplicate = function (nums) {
  return new Set(nums).size !== nums.length;
};
