// 시간복잡도: O(n)

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  // 빈도 계산
  const frequencyMap = new Map();
  for (let num of nums) {
    frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
  }

  // 버킷 정렬
  const bucket = Array(nums.length + 1).fill(null).map(() => []);
  for (let [num, freq] of frequencyMap) {
    bucket[freq].push(num);
  }

  // 빈도 높은 요소들 추출
  const result = [];
  for (let i = bucket.length - 1; i >= 0 && result.length < k; i--) {
    if (bucket[i].length > 0) {
      result.push(...bucket[i]);
    }
  }

  return result.slice(0, k); // 상위 k개의 요소 반환
};

