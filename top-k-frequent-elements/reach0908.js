/**
 * @description
 * time complexity: O(n log n)
 * space complexity: O(n)
 * runtime: 3ms
 * 풀이 방법:
 * 해시맵을 통해 각 숫자의 빈도수를 계산
 * 해시맵을 정렬하여 빈도수가 높은 순서대로 정렬
 * 정렬된 배열을 k만큼 짤라서 반환
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
const topKFrequent = function (nums, k) {
  const hashMap = new Map();

  for (const num of nums) {
    if (hashMap.has(num)) {
      hashMap.set(num, hashMap.get(num) + 1);
    } else {
      hashMap.set(num, 1);
    }
  }

  return Array.from(hashMap.entries())
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map(([num]) => num);
};
