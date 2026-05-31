/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  nums = nums.sort((a, b) => a - b);
  const counter = new Map();
  for (let num of nums) {
    const value = counter.has(num) ? counter.get(num) + 1 : 1;
    counter.set(num, value);
  }
  const sorted = [...counter.entries()].sort((a, b) => b[1] - a[1]);
  const answer = sorted.slice(0, k).map((item) => item[0]);
  // console.log(counter, sorted, answer)

  return answer;
};
