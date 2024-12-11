// https://leetcode.com/problems/top-k-frequent-elements/
function topKFrequent(nums: number[], k: number): number[] {
  const counter = new Map<number, number>();
  for (const n of nums) {
    counter.set(n, (counter.get(n) ?? 0) + 1);
  }
  return [...counter.keys()]
    .sort((a, b) => counter.get(b)! - counter.get(a)!)
    .slice(0, k);
}
