/**
 * 시간 복잡도: O(n)
 * - nums 순회하며 map 생성 O(n)
 * - map 순회하며 bucket 생성 O(n)
 * - bucket 순회하며 결과 찾음 O(n)
 *
 * 공간 복잡도: O(n)
 * - map O(n)
 * - bucket O(n)
 * - result k
 */
const topKFrequent = (nums, k) => {
  // nums 요소 : 요소의 갯수
  const map = {};
  // 요소의 갯수 : Set{ nums 요소 }
  const bucket = [];

  const result = [];

  for (let i = 0; i < nums.length; i += 1) {
    if (map[nums[i]]) {
      map[nums[i]] += 1;
    } else {
      map[nums[i]] = 1;
    }
  }

  for (let [num, freq] of Object.entries(map)) {
    if (bucket[freq]) {
      bucket[freq] = bucket[freq].add(num);
    } else {
      bucket[freq] = new Set().add(num);
    }
  }

  for (let i = bucket.length - 1; i >= 0; i -= 1) {
    if (bucket[i]) {
      // string을 number로 변환
      const value = Array.from(bucket[i], Number);
      result.push(...value);
    }
    if (result.length === k) break;
  }

  return result;
};
