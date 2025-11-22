function topKFrequent(nums: number[], k: number): number[] {
  const numsMap = new Map<number, number>();
  for (let i = 0; i < nums.length; i++) {
    if (numsMap.has(nums[i])) {
      numsMap.set(nums[i], (numsMap.get(nums[i]) ?? 0) + 1);
    } else {
      numsMap.set(nums[i], 1);
    }
  }
  const sortedNums = Array.from(numsMap).sort(([_a, a], [_b, b]) => b - a);
  const results: number[] = [];
  for (let j = 0; j < sortedNums.length && results.length < k; j++) {
    results.push(sortedNums[j][0]);
  }
  return results;
}
