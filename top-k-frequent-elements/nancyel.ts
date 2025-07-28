/**
 * time complexity: O(n + m log m),
 *   n = length of input array
 *   m = number of unique elements (m ≤ n)
 * space complexity: O(m)
 */

function topKFrequent(nums: number[], k: number): number[] {
  const freqMap = new Map<number, number>();

  // Count frequencies using a map: O(n)
  for (const num of nums) {
    freqMap.set(num, (freqMap.get(num) || 0) + 1);
  }

  // Extract the top k elements
  return Array.from(freqMap.entries()) // O(m)
    .sort(([, a], [, b]) => b - a) // O(m log m)
    .slice(0, k)
    .map(([num]) => num); // extract the keys only
}
