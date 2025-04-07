/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
  // Map을 통해 nums의 담긴 숫자들의 빈번함을 정리함.
  const frequencyMap = nums.reduce((map, num) => {
    map.set(num, (map.get(num) || 0) + 1);
    return map;
  }, new Map());

  // 빈도수를 기준으로 정렬하여 답을 유도함.
  const result = Array.from(frequencyMap.entries())
  .sort((a, b) => b[1] - a[1])
  .slice(0, k)
  .map(item => item[0]);

  return result;
};
