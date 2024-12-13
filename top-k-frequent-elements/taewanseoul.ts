/**
 * 347. Top K Frequent Elements
 * Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in
 * any order.
 * https://leetcode.com/problems/top-k-frequent-elements/description/
 */
function topKFrequent(nums: number[], k: number): number[] {
  const map = new Map<number, number>();

  nums.forEach((n) => {
    const count = map.get(n);
    if (count) {
      map.set(n, count + 1);
      return;
    }
    map.set(n, 1);
  });

  const kvArray = [...map];
  const sorted = kvArray.sort(([, v1], [, v2]) => v2 - v1);

  const result: number[] = [];
  for (let i = 0; i < k; i++) {
    result.push(sorted[i][0]);
  }

  return result;
}

// O(n) time
// O(n) space
