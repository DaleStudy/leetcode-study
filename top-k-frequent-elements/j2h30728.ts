/**
 *
 * @param nums
 * @param k
 * @returns
 * 시간 복잡도 : O(n log n)
 * 공간 복잡도 : O(n)
 */
function topKFrequent(nums: number[], k: number): number[] {
  const map = new Map<number, number>();

  for (const num of nums) {
    map.set(num, (map.get(num) ?? 0) + 1);
  }

  const arr = [...map.entries()].sort((a, b) => b[1] - a[1]);

  return arr.slice(0, k).map((x) => x[0]);
}
