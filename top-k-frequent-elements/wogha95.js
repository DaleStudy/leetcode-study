// TC: O(n logn)
// SC: O(N)

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const numAndCountBoard = nums.reduce((result, current) => {
    result[current] = result.hasOwnProperty(current) ? result[current] + 1 : 1;
    return result;
  }, {});

  return Object.entries(numAndCountBoard)
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map((element) => element[0]);
};
