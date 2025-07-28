/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const map = new Map();
  const result = [];

  for (let num of nums) {
    map.set(num, (map.get(num) || 0) + 1);
  }

  const sorted = [...map.entries()]
    .sort((a, b) => b[1] - a[1]) // 빈도 기준으로 정렬
    .map((entry) => entry[0]); // 숫자만 추출

  for (let i = 0; i < k; i++) {
    result.push(sorted[i]);
  }

  return result;
};
