/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

/*
TC: O(nlogn) -> sort
SC: O(n) => numsCount 생성
*/
var topKFrequent = function (nums, k) {
  const numsCount = nums.reduce((acc, cur) => {
    acc[cur] = acc[cur] + 1 || 1;
    return acc;
  }, {});

  const frequecyOrder = Object.entries(numsCount)
    .sort(([, a], [, b]) => b - a)
    .map(([k, v]) => [Number(k), v]);

  const result = [];

  for (let i = 0; i < k; i++) result.push(frequecyOrder[i][0]);

  return result;
};

/*
TC: O(n) -> frequency bucket index로 활용
SC: O(n)
*/
var topKFrequent = function (nums, k) {
  const numsCount = nums.reduce((acc, cur) => {
    acc[cur] = acc[cur] + 1 || 1;
    return acc;
  }, {});

  const bucket = [];
  Object.entries(numsCount).forEach(([num, freq]) => {
    if (!bucket[freq]) bucket[freq] = [];
    bucket[freq].push(Number(num));
  });

  const result = [];
  for (let i = bucket.length - 1; i >= 0 && result.length < k; i--) {
    if (Array.isArray(bucket[i])) {
      result.push(...bucket[i]);
    }
  }

  return result;
};
