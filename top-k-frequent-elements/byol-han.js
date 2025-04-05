/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const freqMap = new Map();

  // 빈도수 계산
  for (const num of nums) {
    freqMap.set(num, (freqMap.get(num) || 0) + 1);
  }

  // Min Heap을 사용해서 상위 k개만 유지
  return Array.from(freqMap.entries()) // [ [num, count], [num, count], ... ]
    .sort((a, b) => b[1] - a[1]) // 빈도수를 기준으로 내림차순 정렬
    .slice(0, k) // 상위 k개 선택
    .map((entry) => entry[0]); // 숫자만 추출

  return result;
};
