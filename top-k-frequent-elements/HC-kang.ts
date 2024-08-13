/*
347. Top K Frequent Elements

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 */

// Time complexity: O(nlogn)
// Space complexity: O(n)
function topKFrequent(nums: number[], k: number): number[] {
  const frequentMap = new Map<number, number>();
  for (const num of nums) { // s.c. O(n)
    frequentMap.set(num, (frequentMap.get(num) || 0) + 1);
  }
  return Array.from(frequentMap.entries())
    .sort((a, b) => b[1] - a[1]) // this will cost t.c. O(nlogn)
    .slice(0, k)
    .map((v) => v[0]);
}
