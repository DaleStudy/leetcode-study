/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const counter = new Map();

  nums.forEach((num) => {
    if (counter.has(num)) {
      counter.set(num, counter.get(num) + 1);
    } else {
      counter.set(num, 1);
    }
  });

  const sorted = [...counter.entries()].sort(
    ([, freqA], [, freqB]) => freqB - freqA
  );

  return sorted.slice(0, k).map(([num]) => num);
};
