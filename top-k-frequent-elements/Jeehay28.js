/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  let result = [];

  const obj = nums.reduce((acc, cur) => {
    acc[cur] = (acc[cur] || 0) + 1;
    return acc;
  }, {});

  const frequentValues = Object.values(obj)
    .sort((a, b) => b - a)
    .slice(0, k);

  for (const [key, value] of Object.entries(obj)) {
    if (frequentValues.includes(value)) {
      result.push(parseInt(key));
    }
  }

  return result;
};
