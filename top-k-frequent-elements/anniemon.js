/**
 * 시간 복잡도:
 * nums.length만큼의 배열을 정렬해야 하므로
 * 즉, O(n * log n)
 * 공간 복잡도:
 * 최대 nums.length만큼의 map 생성
 * 즉, O(n)
 */
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
  const map = new Map();
  for(const n of nums) {
      if(!map.has(n)) {
          map.set(n, 0);
      }
      map.set(n, map.get(n) + 1)
  }
  const sorted = Array.from(map).sort((a, b) => b[1]-a[1]);
  return sorted.slice(0, k).map(e =>  e[0])
};
