/**
 * @param nums - 정수 배열
 * @param k - 자주 등장한 요소의 길이
 * @returns - 자주 등장한 요소들 []
 */
function topKFrequent(nums: number[], k: number): number[] {
  const map = new Map();
  for (const num of nums) {
    if (map.has(num)) {
      map.set(num, map.get(num) + 1);
    } else {
      map.set(num, 1);
    }
  }

  const sorted = Array.from(map)
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map((v) => v[0]);
  return sorted;
}

topKFrequent([1, 1, 1, 2, 2, 3], 2);
